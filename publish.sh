#!/bin/bash

# Facial Recognition System - GitHub Publishing Script
# This script helps you publish your project to GitHub

echo "🚀 Facial Recognition System - GitHub Publisher"
echo "================================================"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

echo "✅ Git is installed"
echo ""

# Check if already initialized
if [ -d ".git" ]; then
    echo "⚠️  Git repository already initialized"
    echo ""
    read -p "Do you want to continue? (y/n): " continue
    if [ "$continue" != "y" ]; then
        echo "Aborted."
        exit 0
    fi
else
    echo "📦 Initializing Git repository..."
    git init
    echo "✅ Git repository initialized"
    echo ""
fi

# Get GitHub username
echo "Please enter your GitHub username:"
read github_username

if [ -z "$github_username" ]; then
    echo "❌ GitHub username cannot be empty"
    exit 1
fi

echo ""
echo "📝 Your GitHub username: $github_username"
echo ""

# Get repository name
echo "Enter repository name (default: facial-recognition-system):"
read repo_name

if [ -z "$repo_name" ]; then
    repo_name="facial-recognition-system"
fi

echo ""
echo "📝 Repository name: $repo_name"
echo ""

# Update README with username
echo "📝 Updating README.md with your GitHub username..."
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    sed -i '' "s/yourusername/$github_username/g" README.md
    sed -i '' "s/yourusername/$github_username/g" PUBLISH_TO_GITHUB.md
    sed -i '' "s/yourusername/$github_username/g" QUICKSTART.md
else
    # Linux
    sed -i "s/yourusername/$github_username/g" README.md
    sed -i "s/yourusername/$github_username/g" PUBLISH_TO_GITHUB.md
    sed -i "s/yourusername/$github_username/g" QUICKSTART.md
fi
echo "✅ Files updated"
echo ""

# Add all files
echo "📦 Adding files to Git..."
git add .
echo "✅ Files added"
echo ""

# Create commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Facial Recognition System MVP

- Complete facial recognition system
- Web-based dashboard
- Deep learning face detection
- Professional documentation
- Real screenshots included
- Ready for deployment"
echo "✅ Commit created"
echo ""

# Set main branch
echo "🌿 Setting main branch..."
git branch -M main
echo "✅ Main branch set"
echo ""

# Add remote
echo "🔗 Adding remote repository..."
git remote add origin "https://github.com/$github_username/$repo_name.git"
echo "✅ Remote added"
echo ""

echo "================================================"
echo "✅ Local setup complete!"
echo ""
echo "📋 Next steps:"
echo ""
echo "1. Go to https://github.com/new"
echo "2. Create a new repository named: $repo_name"
echo "3. Make it PUBLIC"
echo "4. DO NOT initialize with README"
echo "5. Click 'Create repository'"
echo ""
echo "Then run:"
echo "  git push -u origin main"
echo ""
echo "================================================"
echo ""
echo "🎉 Your project will be live at:"
echo "   https://github.com/$github_username/$repo_name"
echo ""
echo "Don't forget to:"
echo "  ⭐ Star your own repo"
echo "  📝 Add topics/tags"
echo "  🔗 Share on social media"
echo ""
echo "Good luck! 🚀"
