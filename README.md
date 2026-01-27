# Project Name

## 📋 Interactive Task Grid

**[View Interactive Task Grid →](https://yourusername.github.io/yourrepo/task-grid.html)**

Browse and search all tasks with filters for difficulty, location, and more!

---

## Quick Setup Instructions

### 1. Enable GitHub Pages
1. Go to your repository Settings
2. Navigate to "Pages" in the left sidebar
3. Under "Source", select the branch (usually `main` or `master`)
4. Click "Save"
5. Your page will be available at `https://yourusername.github.io/yourrepo/task-grid.html`

### 2. Update the Task Data
Edit the `tasks` array in `task-grid.html` (around line 193) with your actual tasks:

```javascript
const tasks = [
    { 
        number: 1, 
        description: "Your task description", 
        difficulty: "easy", // or "medium" or "hard"
        location: "path/to/file.py", 
        notes: "Any additional notes" 
    },
    // Add more tasks...
];
```

### 3. Update the README Link
Replace `yourusername` and `yourrepo` in the link above with your actual GitHub username and repository name.

---

## Features

✨ **Real-time filtering** - Search updates as you type  
🎨 **GitHub-themed design** - Matches GitHub's dark mode aesthetic  
📱 **Responsive** - Works on mobile and desktop  
🔍 **Multi-column search** - Filter by task number, description, difficulty, location, or notes  
🎯 **Difficulty badges** - Color-coded easy/medium/hard labels

---

## Task Overview

| Difficulty | Count |
|------------|-------|
| Easy       | X     |
| Medium     | Y     |
| Hard       | Z     |

For the full interactive list with search and filtering, visit the **[Task Grid](https://yourusername.github.io/yourrepo/task-grid.html)**.

---

## Alternative: Static Table in README

If you prefer to keep everything in the README (without interactivity), you can use a static table:

<details>
<summary>Click to expand task list</summary>

| # | Description | Difficulty | Location | Notes |
|---|-------------|------------|----------|-------|
| 1 | Implement binary search | Easy | algorithms/search.py | Use iterative approach |
| 2 | Create REST API endpoint | Medium | api/auth.js | Include JWT tokens |
| 3 | Optimize database queries | Hard | database/queries.sql | Add proper indexes |

</details>

---

## Contributing

To add a new task:
1. Edit the `tasks` array in `task-grid.html`
2. Commit and push your changes
3. GitHub Pages will automatically update

## License

MIT
