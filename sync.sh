#!/bin/bash
# sync.sh — Automatic CS50 private-to-public synchronization
# Author: Caio Santos
# Enhanced version with automatic dated commits and rebase safety

set -e

# --- COLORS ---
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
NC="\033[0m" # no color

echo -e "${YELLOW}🔍 Checking current branch...${NC}"
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
  echo -e "${YELLOW}⚠️  Switching to 'main'...${NC}"
  git checkout main
fi

# --- Handle unfinished rebase ---
if [ -d ".git/rebase-merge" ] || [ -d ".git/rebase-apply" ]; then
  echo -e "${RED}⚠️  Rebase detected! Aborting previous rebase...${NC}"
  git rebase --abort || true
  rm -rf .git/rebase-merge .git/rebase-apply || true
fi

# --- Sync with public repo first ---
echo -e "${YELLOW}🔄 Pulling latest changes from public repo (origin)...${NC}"
git fetch origin
git pull --rebase origin main || true

# --- Fetch from private repo ---
echo -e "${YELLOW}📡 Fetching updates from private repo (cs50)...${NC}"
git fetch cs50

# --- Check if new commits exist ---
LOCAL_HASH=$(git rev-parse main)
REMOTE_HASH=$(git rev-parse cs50/main)

if [ "$LOCAL_HASH" == "$REMOTE_HASH" ]; then
  echo -e "${GREEN}✅ Everything is already up to date!${NC}"
else
  # --- Merge new commits from cs50/main ---
  echo -e "${YELLOW}🧩 Merging new commits from CS50...${NC}"
  git merge cs50/main --no-edit
fi

# --- Restore public-only files (README, LICENSE, etc) ---
echo -e "${YELLOW}🚫 Restoring public-only files...${NC}"
git restore README.md 2>/dev/null || true
git restore LICENSE 2>/dev/null || true

# --- Check for local modifications and commit if needed ---
if [ -n "$(git status --porcelain)" ]; then
  echo -e "${YELLOW}📝 Changes detected — creating timestamped commit...${NC}"
  COMMIT_MSG=$(date +"%a, %b %d, %Y, %I:%M %p %z")
  git add .
  git commit -m "$COMMIT_MSG"
else
  echo -e "${GREEN}✨ No local modifications to commit.${NC}"
fi

# --- Push to public repo ---
echo -e "${YELLOW}🚀 Pushing to public repo (origin)...${NC}"
git push origin main

echo -e "${GREEN}🎉 Synchronization completed successfully at $(date +"%I:%M %p")!${NC}"
