import os
import re

def extract_metadata(file_path):
    title = "Unknown Title"
    description = "No description provided."
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if not lines: return title, description

            # 1. Clean Title: Remove the '#' and the 'n' typo if it exists
            raw_title = lines[0].strip('# ').strip()
            # Fix common "nConstruct" typos or extra 'n's at the start
            title = re.sub(r'^[nN](?=[A-Z])', '', raw_title) 
            
            # 2. Extract Description
            desc_parts = []
            for line in lines[1:]:
                clean = line.strip()
                
                # STOP if we hit the class, the personal notes, or an empty line
                if "class" in clean or "I had" in clean or "Confussed" in clean:
                    break
                
                # Only add if it's a comment and not empty
                if clean.startswith('#'):
                    content = clean.strip('# ').strip()
                    if content:
                        desc_parts.append(content)
                elif not clean: # Skip empty lines but keep looking
                    continue
                else: # Hit actual code that isn't the class
                    break
            
            if desc_parts:
                description = " ".join(desc_parts[:3]) # Take first 3 lines
                if len(description) > 120:
                    description = description[:117] + "..."
                    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        
    return title, description

def generate_readme():
    base_dir = "2026"
    months_order = ["January", "February", "March", "April", "May", "June", 
                    "July", "August", "September", "October", "November", "December"]
    
    readme_content = "# 📖 LeetCode Journey 2026\n\n"
    readme_content += "This repository automatically tracks my LeetCode progress using a custom Python scraper.\n\n"

    if not os.path.exists(base_dir):
        print(f"Error: Folder '{base_dir}' not found.")
        return

    # Sort months based on the calendar
    found_months = [m for m in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, m))]
    sorted_months = sorted(found_months, key=lambda x: months_order.index(x) if x in months_order else 99)

    for month in sorted_months:
        month_path = os.path.join(base_dir, month)
        # Sort files numerically by the "day" number
        files = sorted(os.listdir(month_path), key=lambda x: int(re.search(r'day (\d+)', x).group(1)) if re.search(r'day (\d+)', x) else 0)
        
        if not files:
            continue

        readme_content += f"## 📅 {month}\n"
        readme_content += "| ID | Problem Title | Description | Solution |\n"
        readme_content += "| :--- | :--- | :--- | :--- |\n"

        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(month_path, file)
                title, description = extract_metadata(full_path)
                
                # Regex to extract the Problem ID from inside the parentheses
                id_match = re.search(r"\((\d+)\)", file)
                prob_id = id_match.group(1) if id_match else "N/A"
                
                # URL encode spaces for Markdown links
                encoded_path = f"./2026/{month}/{file}".replace(" ", "%20")
                
                readme_content += f"| {prob_id} | {title} | {description} | [View Code]({encoded_path}) |\n"
        
        readme_content += "\n---\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print("✨ Success! README.md updated with titles and descriptions.")

if __name__ == "__main__":
    generate_readme()