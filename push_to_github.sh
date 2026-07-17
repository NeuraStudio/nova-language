#!/bin/bash
echo "🚀 [NeuraGit™] Connecting to GitHub..."

# Initialize git if not already done
git init

# Add all 400+ folders, C++ core, and website files
git add .

# Commit the code
echo "Enter commit message (or press enter for default):"
read commit_msg
if [ -z "$commit_msg" ]; then
    commit_msg="Nova Language: Core Ecosystem & Web IDE Update"
fi
git commit -m "$commit_msg"

echo "✅ Code committed locally!"
echo "⚠️ IMPORTANT: To make it live on GitHub, create a new repo on GitHub.com"
echo "Then run these two commands in Termux:"
echo "1. git remote add origin <YOUR_GITHUB_REPO_URL>"
echo "2. git push -u origin main"
echo ""
echo "To host the website, go to GitHub Repo Settings -> Pages -> Deploy from branch (main) -> /website folder."
