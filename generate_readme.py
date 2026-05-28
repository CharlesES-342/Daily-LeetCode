import os
import re

def extract_metadata(file_path):
    title = "Unknown Title"
    description = "No description provided."
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if not lines: return title, description

            # 1. Clean Title
            raw_title = lines[0].strip('# ').strip()
            title = re.sub(r'^[nN](?=[A-Z])', '', raw_title) 
            
            # 2. Extract Description
            desc_parts = []
            for line in lines[1:]:
                clean = line.strip()
                if any(x in clean for x in ["class", "I had", "Confussed"]):
                    break
                if clean.startswith('#'):
                    content = clean.strip('# ').strip()
                    if content:
                        desc_parts.append(content)
                elif not clean:
                    continue
                else:
                    break
            
            if desc_parts:
                description = " ".join(desc_parts[:3])
                if len(description) > 120:
                    description = description[:117] + "..."
                    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        
    return title, description

def generate_readme():
    months_order = ["January", "February", "March", "April", "May", "June", 
                    "July", "August", "September", "October", "November", "December"]
    
    # 1. Dynamically find all Year folders (4-digit names)
    years = sorted([d for d in os.listdir('.') if os.path.isdir(d) and re.match(r'^\d{4}$', d)], reverse=True)
    
    total_solved = 0
    full_content = ""
    year_nav = []

    for year in years:
        year_nav.append(f"[**{year}**](#-year-{year})")
        year_section = f"## 📅 Year {year}\n"
        
        found_months = [m for m in os.listdir(year) if os.path.isdir(os.path.join(year, m))]
        sorted_months = sorted(found_months, key=lambda x: months_order.index(x) if x in months_order else 99)

        for month in sorted_months:
            month_path = os.path.join(year, month)
            py_files = [f for f in os.listdir(month_path) if f.endswith(".py")]
            
            if not py_files:
                continue

            total_solved += len(py_files)

            # --- SORTING LOGIC ---
            # Sorts by Day Number AND Problem ID simultaneously 
            def sort_key(filename):
                day_match = re.search(r'day (\d+)', filename, re.IGNORECASE)
                id_match = re.search(r'\((\d+)\)', filename)
                day_val = int(day_match.group(1)) if day_match else 0
                id_val = int(id_match.group(1)) if id_match else 0
                return (day_val, id_val)

            py_files.sort(key=sort_key)

            # Enhanced Summary Layout
            year_section += f"### {month}\n"
            year_section += f"<details>\n<summary><b>📂 View {month} {year} Progress ({len(py_files)} Problems)</b></summary>\n\n"
            year_section += "| ID | Problem Title | Description | Solution |\n"
            year_section += "| :--- | :--- | :--- | :--- |\n"

            for file in py_files:
                full_path = os.path.join(month_path, file)
                title, description = extract_metadata(full_path)
                
                id_match = re.search(r"\((\d+)\)", file)
                prob_id = id_match.group(1) if id_match else "N/A"
                
                # Fix pathing for multiple years
                encoded_path = f"./{year}/{month}/{file}".replace(" ", "%20")
                year_section += f"| `{prob_id}` | **{title}** | {description} | [View Code]({encoded_path}) |\n"
            
            year_section += "\n</details>\n\n"
        
        full_content += year_section + "---\n"

    # 3. Assemble Header and Navigation
    header = "# 📖 LeetCode Journey\n\n"
    header += f"**🚀 Total Problems Solved: {total_solved}**\n\n"
    header += "This repository tracks my LeetCode progress across multiple years.\n\n"
    header += "### 🔍 Quick Navigation\n"
    header += " | ".join(year_nav) + "\n\n---\n\n"

    # 4. Write to File
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(header + full_content)
    
    print(f"✨ Success! README updated. Total years: {len(years)} | Total solved: {total_solved}")

if __name__ == "__main__":
    generate_readme()