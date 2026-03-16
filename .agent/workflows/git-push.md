---
description: How to commit and push code to GitHub from this project
---

# ⚠️ CRITICAL: PowerShell Rules
**NEVER use `&&` to chain commands in PowerShell.**  
PowerShell does NOT support `&&`. It will throw a parser error.  
**Always use `;` to chain commands instead.**

✅ Correct:   `git add .; git status`  
❌ Wrong:     `git add . && git status`  

---

# Git Push Workflow

1. Stage all changes:
```
git add .
```

2. Check what's staged:
```
git status
```

3. Commit with a descriptive message:
```
git commit -m "your message here"
```

4. Push to main:
```
git push origin main
```
