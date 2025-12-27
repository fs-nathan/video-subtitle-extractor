#!/bin/bash
# Script để remove các file lớn khỏi git tracking
# Chạy script này nếu các file đã được commit trước đó

cd "$(dirname "$0")"

echo "🧹 Removing large files from git tracking..."
echo ""

# Remove models (512MB)
if git ls-files --error-unmatch backend/models/ >/dev/null 2>&1; then
    echo "Removing backend/models/ (512MB)..."
    git rm -r --cached backend/models/ 2>/dev/null
fi

# Remove test videos
echo "Removing test videos..."
git rm --cached test/*.mp4 test/*.flv test/*.avi 2>/dev/null || true

# Remove user videos
if git ls-files --error-unmatch mukbang/ >/dev/null 2>&1; then
    echo "Removing mukbang/ (46MB)..."
    git rm -r --cached mukbang/ 2>/dev/null
fi

# Remove output
if git ls-files --error-unmatch output/ >/dev/null 2>&1; then
    echo "Removing output/..."
    git rm -r --cached output/ 2>/dev/null
fi

# Remove virtual environments
if git ls-files --error-unmatch videoEnv/ >/dev/null 2>&1; then
    echo "Removing videoEnv/..."
    git rm -r --cached videoEnv/ 2>/dev/null
fi

if git ls-files --error-unmatch videoEnv312/ >/dev/null 2>&1; then
    echo "Removing videoEnv312/..."
    git rm -r --cached videoEnv312/ 2>/dev/null
fi

# Remove config files
echo "Removing config files..."
git rm --cached settings.ini subtitle.ini 2>/dev/null || true

# Remove temporary files
echo "Removing temporary files..."
git rm --cached test_run*.py test_output.log 2>/dev/null || true
git rm --cached *_FIX.md *_INSTRUCTIONS.md EXPLAIN_*.md COLAB_FIX.md SOLUTION.md TROUBLESHOOTING.md QUICK_FIX.md SETUP_COMPLETE.md RUN_GUI*.sh 2>/dev/null || true

echo ""
echo "✅ Done! Files removed from git tracking (but kept locally)"
echo ""
echo "Next steps:"
echo "1. git add .gitignore"
echo "2. git commit -m 'Remove large files from git tracking'"
echo "3. git push"
echo ""
echo "⚠️  Note: If files were already pushed, they still exist in git history."
echo "   Consider using 'git filter-branch' or creating a new repo."

