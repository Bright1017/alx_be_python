#!/bin/bash

# Check if a commit message is provided as an argument
if [ -z "$1" ]; then
  echo "❌ Error: Commit message is required."
  echo "Usage: ./git-auto.sh 'Your commit message here'"
  exit 1
fi

# Add, commit, and push changes
git add .
git commit -m "$1"
git push

echo "✅ Changes have been successfully pushed!"