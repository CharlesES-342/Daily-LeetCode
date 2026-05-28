import os
import re

def extract_metadata(file_path):
    title = "Unknown Title"
    description = "No description provided."
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if not lines: return title, description

            # Clean Title: Remove '#' and handle 'n' typo
            raw_title = lines[0].strip('# ').strip()
            title = re.sub(r'^[nN](?=[A-Z])', '', raw_title) 
            
            # Extract Description
            desc_parts = []
            for line in lines[1:]:
                clean = line.strip()
                if any(x in clean.lower() for x in ["class", "i had", "confussed"]):
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
    # Configuration
    months_order = ["January", "February", "March", "April", "May", "June", 
                    "July", "August", "September", "October", "November", "December"]
    
    # 1. Identify Year Folders (4-digit names)
    years = sorted([d for d in os.listdir('.') if os.path.isdir(d) and re.match(r'^\d{4}$', d)], reverse=True)
    
    total_solved = 0
    full_body = ""
    year_links = []

    for year in years:
        year_links.append(f"[**{year}**](#year-{year})")
        year_content = f"## 📅 Year {year} <a name='year-{year}'></a>\n\n"
        
        found_months = [m for m in os.listdir(year) if os.path.isdir(os.path.join(year, m))]
        # Sort months chronologically
        sorted_months = sorted(found_months, key=lambda x: months_order.index(x) if x in months_order else 99)

        for month in sorted_months:
            month_path = os.path.join(year, month)
            all_files = [f for f in os.listdir(month_path) if f.endswith(".py")]
            
            if not all_files:
                continue

            # --- SORTING LOGIC ---
            # Default: Sort by Day Number (Extracted from "day X")
            all_files.sort(key=lambda x: int(re.search(r'day (\d+)', x, re.IGNORECASE).group(1)) if re.search(r'day (\d+)', x, re.IGNORECASE) else 0)
            
            # Alternative: Sort by Problem ID (Extracted from "(123)")
            # all_files.sort(key=lambda x: int(re.search(r'\((\d+)\)', x).group(1)) if re.search(r'\((\d+)\)', x) else 99999)

            total_solved += len(all_files)
            
            # Prettier Summary UI
            year_content += f"### {month}\n"
            year_content += f"<details>\n<summary><b>📂 Click to expand {month} {year} ({len(all_files)} problems)</b></summary>\n\n"
            year_content += "| ID | Problem Title | Description | Solution |\n"
            year_content += "| :--- | :--- | :--- | :--- |\n"

            for file in all_files:
                full_path = os.path.join(month_path, file)
                title, description = extract_metadata(full_path)
                
                id_match = re.search(r"\((\d+)\)", file)
                prob_id = id_match.group(1) if id_match else "N/A"
                
                encoded_path = f"./{year}/{month}/{file}".replace(" ", "%20")
                year_content += f"| `{prob_id}` | **{title}** | {description} | [View Code]({encoded_path}) |\n"
            
            year_content += "\n</details>\n\n"
        
        full_body += year_content + "---\n"

    # 3. Assemble Final Header
    header = "# 📖 LeetCode Journey\n\n"
    header += f"**🚀 Total Problems Solved: {total_solved}**\n\n"
    header += "This repository automatically tracks progress across multiple years using a GitHub Actions workflow.\n\n"
    header += "### 🔍 Jump to Year\n"
    header += f"{' | '.join(year_links)}\n\n---\n\n"

    # 4. Write to File
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(header + full_body)
    
    print(f"✨ Success! README updated for {len(years)} years. Total solved: {total_solved}")

if __name__ == "__main__":
    generate_readme()