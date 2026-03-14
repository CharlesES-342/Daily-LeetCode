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
    base_dir = "2026"
    # Your specific repository URL
    repo_url = "https://github.com/CharlesES-342/Daily-LeetCode" 
    
    months_order = ["January", "February", "March", "April", "May", "June", 
                    "July", "August", "September", "October", "November", "December"]
    
    if not os.path.exists(base_dir):
        print(f"Error: Folder '{base_dir}' not found.")
        return

    # 1. Identify and Sort Months
    found_months = [m for m in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, m))]
    # Sort months based on the calendar order defined in months_order
    sorted_months = sorted(found_months, key=lambda x: months_order.index(x) if x in months_order else 99)

    # 2. Pre-calculate total solved count and prepare tables
    total_solved = 0
    tables_content = ""

    for i, month in enumerate(sorted_months):
        month_path = os.path.join(base_dir, month)
        # Sort files numerically by the "day" number found in the filename
        all_files = os.listdir(month_path)
        files = sorted(all_files, key=lambda x: int(re.search(r'day (\d+)', x, re.IGNORECASE).group(1)) if re.search(r'day (\d+)', x, re.IGNORECASE) else 0)
        
        py_files = [f for f in files if f.endswith(".py")]
        if not py_files:
            continue

        total_solved += len(py_files)

        # Logic: Keep only the most recent month 'open' by default
        # If you prefer ALL months to be open, simply set is_open = "open"
        is_open = "open" if i == len(sorted_months) - 1 else ""

        # Build Month Section
        tables_content += f"## 📅 {month}\n"
        tables_content += f"<details {is_open}>\n<summary>Click to view {month} problems</summary>\n\n"
        tables_content += "| ID | Problem Title | Description | Solution |\n"
        tables_content += "| :--- | :--- | :--- | :--- |\n"

        for file in py_files:
            full_path = os.path.join(month_path, file)
            title, description = extract_metadata(full_path)
            
            # Extract Problem ID from parentheses, e.g., Day 1 - (66).py -> 66
            id_match = re.search(r"\((\d+)\)", file)
            prob_id = id_match.group(1) if id_match else "N/A"
            
            encoded_path = f"./2026/{month}/{file}".replace(" ", "%20")
            tables_content += f"| {prob_id} | {title} | {description} | [View Code]({encoded_path}) |\n"
        
        tables_content += "\n</details>\n\n---\n"

    # 3. Assemble the Header and Navigation
    jump_links = " | ".join([f"[**{m}**](#-{m.lower()})" for m in sorted_months])
    
    header = "# 📖 LeetCode Journey 2026\n\n"
    header += f"**Total Problems Solved: {total_solved}**\n\n"
    header += "This repository automatically tracks my LeetCode progress using a custom Python scraper.\n\n"
    header += "### 🔍 Quick Navigation\n"
    header += f"{jump_links} | [**Search by ID**]({repo_url}/search?q=)\n\n"
    header += "---\n\n"

    # 4. Write to File
    with open("README.md", "w", encoding="utf-8")

if __name__ == "__main__":
    generate_readme()
