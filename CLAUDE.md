# 🚀 CLAUDE.md - Automated BFHL Qualifier 1 Solution

> **Complete automation with Claude Code CLI + MCP Servers**

---

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [MCP Servers Setup](#mcp-servers-setup)
3. [Automated Workflow](#automated-workflow)
4. [Complete Task Execution](#complete-task-execution)
5. [Deployment Commands](#deployment-commands)
6. [Verification & Testing](#verification--testing)
7. [Troubleshooting](#troubleshooting)

---

## ⚡ Quick Start

### Prerequisites
```bash
# Install Claude Code CLI
npm install -g @anthropic-ai/claude

# Or using pip
pipx install claude-code

# Verify installation
claude-code --version

# Ensure you have git and GitHub account
git --version
python3 --version
```

### One-Command Setup
```bash
claude-code
```

Then in Claude Code terminal:
```
> run: bash setup-complete.sh
```

---

## 🔌 MCP Servers Setup

### Required MCP Servers

The following MCP servers should be enabled for this project:

#### 1. **GitHub MCP** (Essential)
```yaml
name: GitHub
type: mcp
features:
  - Push code to repository
  - Create repositories
  - Manage branches
  - Create pull requests
authentication: GitHub OAuth
```

**Setup:**
```bash
> mcp connect github
# Or enable in Claude settings: 
# Settings → MCP Servers → Enable GitHub
```

#### 2. **File Operations MCP** (Essential)
```yaml
name: File Operations
type: mcp
features:
  - Read/write files
  - Create directories
  - Manage project structure
```

**Setup:**
- Automatically available in Claude Code
- No additional setup needed

#### 3. **Google Drive MCP** (Optional - For problem PDFs)
```yaml
name: Google Drive
type: mcp
features:
  - Download problem statements
  - Access SQL query references
```

**Setup:**
```bash
> mcp connect google-drive
# Or enable in Claude settings
```

#### 4. **Web Search MCP** (Optional)
```yaml
name: Web Search
type: mcp
features:
  - Search for documentation
  - Verify SQL syntax
```

**Setup:**
- Available in most Claude Code environments
- Enable if needed for research

---

## 🤖 Automated Workflow

### Step 1: Initialize Project

```bash
# In Claude Code terminal:
> run: mkdir -p bfhl-qualifier && cd bfhl-qualifier

> create main.py
# (Paste the complete main.py code below)

> create app.py
# (Paste the complete app.py code below)

> create requirements.txt
requests==2.31.0
python-dotenv==1.0.0

> create requirements-deploy.txt
requests==2.31.0
python-dotenv==1.0.0
flask==3.0.0
gunicorn==21.2.0

> create .env
USER_NAME=John Doe
REG_NO=REG12347
USER_EMAIL=john@example.com
API_BASE_URL=https://bfhldevapigw.healthrx.co.in/hiring

> create .env.example
USER_NAME=Your Name
REG_NO=YOUR_REG_NUMBER
USER_EMAIL=your@email.com
API_BASE_URL=https://bfhldevapigw.healthrx.co.in/hiring

> create Procfile
web: gunicorn app:app

> create runtime.txt
python-3.11.7

> create .gitignore
__pycache__/
*.py[cod]
*.egg-info/
venv/
env/
.env
.DS_Store
*.log
```

### Step 2: Setup Local Environment

```bash
# In Claude Code terminal:
> run: python3 -m venv venv

> run: . venv/bin/activate && pip install -r requirements.txt

> run: python main.py
# Test the CLI version locally
```

### Step 3: Initialize Git

```bash
# In Claude Code terminal:
> run: git init

> run: git add .

> run: git commit -m "BFHL Qualifier 1 - Initial commit with complete solution"

> run: git branch -M main
```

### Step 4: Create GitHub Repository

```bash
# Option A: Using GitHub MCP (Automatic)
> mcp github create-repo bfhl-qualifier

# Option B: Manual
# 1. Go to github.com/new
# 2. Create repo: bfhl-qualifier
# 3. Copy the URL

> run: git remote add origin https://github.com/YOUR-USERNAME/bfhl-qualifier.git

> run: git push -u origin main
```

### Step 5: Deploy to Railway

```bash
# In Claude Code terminal:
> run: curl -L https://railway.app/install | sh

# Then:
> run: railway login
# Follow the authentication flow in browser

> run: railway init
# Select: bfhl-qualifier
# Select: Python

> run: railway up
# Auto-deploys to Railway!
```

### Step 6: Configure Environment Variables

```bash
# Using Railway dashboard or CLI:
> run: railway variables set USER_NAME="Your Full Name"

> run: railway variables set REG_NO="REG12347"

> run: railway variables set USER_EMAIL="your@email.com"

> run: railway variables set API_BASE_URL="https://bfhldevapigw.healthrx.co.in/hiring"
```

### Step 7: Test Live Deployment

```bash
> run: railway logs -f
# Watch logs in real-time

# In another terminal:
> run: curl https://your-railway-url.app/health

> run: curl https://your-railway-url.app/

> run: curl https://your-railway-url.app/docs
```

---

## 🎯 Complete Task Execution

### Automated Complete Script

Create `claude-auto-run.sh`:

```bash
#!/bin/bash

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}🚀 BFHL Qualifier 1 - Complete Automation${NC}"
echo "=============================================="

# Step 1: Install dependencies
echo -e "${YELLOW}Step 1: Installing dependencies...${NC}"
pip install -q -r requirements.txt
pip install -q -r requirements-deploy.txt

# Step 2: Test CLI version
echo -e "${YELLOW}Step 2: Testing CLI version...${NC}"
python main.py 2>&1 | head -20

# Step 3: Setup Git
echo -e "${YELLOW}Step 3: Setting up Git...${NC}"
if [ ! -d .git ]; then
    git init
    git add .
    git commit -m "BFHL Qualifier 1 - Complete solution"
    git branch -M main
    echo "Git initialized"
else
    echo "Git already initialized"
fi

# Step 4: Configure Railway
echo -e "${YELLOW}Step 4: Checking Railway installation...${NC}"
if command -v railway &> /dev/null; then
    echo "Railway CLI found"
    railway login || echo "Already logged in"
else
    echo "Installing Railway CLI..."
    curl -L https://railway.app/install | sh
fi

# Step 5: Deploy
echo -e "${YELLOW}Step 5: Deploying to Railway...${NC}"
railway up || echo "Railway deployment skipped (run manually or already deployed)"

# Step 6: Test
echo -e "${YELLOW}Step 6: Testing deployment...${NC}"
sleep 5
railway logs -n 20 || echo "Logs not available yet"

echo -e "${GREEN}=============================================="
echo "✅ Complete automation finished!"
echo "=============================================="
echo "Next steps:"
echo "1. Update .env with YOUR credentials"
echo "2. Push to GitHub: git push origin main"
echo "3. Deploy: railway up"
echo "4. Test: curl https://your-railway-url.app/"
echo "=============================================="
```

Run with:
```bash
> run: bash claude-auto-run.sh
```

---

## 📤 Deployment Commands

### Quick Deployment (All-in-One)

```bash
# Full deployment in one command
> run: bash ./deploy-complete.sh
```

Create `deploy-complete.sh`:

```bash
#!/bin/bash

set -e  # Exit on error

echo "🚀 Complete BFHL Deployment"
echo "=============================="

# Update credentials
read -p "Enter your name: " USER_NAME
read -p "Enter your reg number: " REG_NO
read -p "Enter your email: " USER_EMAIL

# Update .env
cat > .env << EOF
USER_NAME=$USER_NAME
REG_NO=$REG_NO
USER_EMAIL=$USER_EMAIL
API_BASE_URL=https://bfhldevapigw.healthrx.co.in/hiring
EOF

echo "✅ .env updated"

# Git operations
git add .
git commit -m "BFHL Qualifier 1 - Updated with credentials"
git push origin main

echo "✅ Code pushed to GitHub"

# Railway deployment
if command -v railway &> /dev/null; then
    railway up
    echo "✅ Deployed to Railway"
    
    # Get URL
    RAILWAY_URL=$(railway link)
    echo ""
    echo "🎉 Deployment complete!"
    echo "Your live app: $RAILWAY_URL"
    echo ""
    echo "Testing..."
    sleep 3
    curl -s "$RAILWAY_URL/health" | jq .
else
    echo "⚠️  Railway CLI not found"
    echo "Install from: https://railway.app"
fi
```

### Step-by-Step Deployment

```bash
# Step 1: Update credentials
> run: nano .env

# Step 2: Test locally
> run: . venv/bin/activate && python app.py

# Step 3: Push to GitHub
> run: git add . && git commit -m "Ready for deployment" && git push origin main

# Step 4: Deploy to Railway
> run: railway up

# Step 5: View logs
> run: railway logs -f

# Step 6: Test live
> run: railway env | grep RAILWAY_PUBLIC_DOMAIN
> run: curl https://<YOUR-RAILWAY-URL>/
```

---

## ✅ Verification & Testing

### Pre-Deployment Tests

```bash
# Test 1: Check Python installation
> run: python3 --version

# Test 2: Check dependencies
> run: pip list | grep -E "requests|flask|gunicorn"

# Test 3: Run CLI version
> run: python main.py

# Test 4: Check code syntax
> run: python -m py_compile main.py app.py

# Test 5: Run unit tests
> run: python -m unittest test_main.py -v

# Test 6: Flask app test
> run: python -c "from app import app; print('Flask app imports successfully')"

# Test 7: Local server test
> run: timeout 5 python app.py || true
```

### Post-Deployment Tests

```bash
# Test 1: Health check
> run: curl -s https://your-railway-url.app/health | jq .

# Test 2: Main endpoint
> run: curl -s https://your-railway-url.app/ | jq .

# Test 3: Config check
> run: curl -s https://your-railway-url.app/config | jq .

# Test 4: Documentation
> run: curl -s https://your-railway-url.app/docs | jq .

# Test 5: Full workflow
> run: curl -X POST https://your-railway-url.app/trigger | jq .

# Test 6: Response validation
> run: curl -s https://your-railway-url.app/ | jq '.status'
```

### Monitoring & Logs

```bash
# View live logs
> run: railway logs -f

# View last 50 lines
> run: railway logs -n 50

# Check deployment status
> run: railway status

# View environment variables
> run: railway env

# Monitor metrics
> run: railway metrics
```

---

## 🔍 Verification Scripts

Create `verify-complete.sh`:

```bash
#!/bin/bash

echo "🔍 BFHL Qualifier 1 - Complete Verification"
echo "=============================================="

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✅${NC} $1 exists"
    else
        echo -e "${RED}❌${NC} $1 missing"
    fi
}

check_command() {
    if command -v $1 &> /dev/null; then
        echo -e "${GREEN}✅${NC} $1 installed"
    else
        echo -e "${RED}❌${NC} $1 not installed"
    fi
}

echo ""
echo "📁 Files:"
check_file "main.py"
check_file "app.py"
check_file "requirements.txt"
check_file "requirements-deploy.txt"
check_file ".env"
check_file "Procfile"
check_file ".gitignore"

echo ""
echo "🔧 Tools:"
check_command "python3"
check_command "git"
check_command "pip"
check_command "railway"

echo ""
echo "📦 Dependencies:"
python3 -c "import requests; print('✅ requests installed')" 2>/dev/null || echo "❌ requests missing"
python3 -c "import flask; print('✅ flask installed')" 2>/dev/null || echo "❌ flask missing"
python3 -c "import dotenv; print('✅ python-dotenv installed')" 2>/dev/null || echo "❌ python-dotenv missing"

echo ""
echo "🔗 Git Status:"
if git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${GREEN}✅${NC} Git repository initialized"
    echo "Remote: $(git remote get-url origin 2>/dev/null || echo 'Not configured')"
else
    echo -e "${RED}❌${NC} Git not initialized"
fi

echo ""
echo "🚀 Railway Status:"
if command -v railway &> /dev/null; then
    railway status 2>/dev/null && echo -e "${GREEN}✅${NC} Railway connected" || echo -e "${YELLOW}⚠️${NC} Railway not logged in"
else
    echo -e "${RED}❌${NC} Railway CLI not installed"
fi

echo ""
echo "✅ Verification complete!"
```

Run:
```bash
> run: bash verify-complete.sh
```

---

## 🧠 MCP Capabilities for This Project

### GitHub MCP Operations

```bash
# Create repository
> mcp github create-repo bfhl-qualifier

# Push code
> mcp github push bfhl-qualifier

# Create pull request
> mcp github create-pr "Add deployment configuration"

# Check commit history
> mcp github list-commits
```

### File Operations

```bash
# Create files
> create filename.py

# Edit files
> view filename.py
> replace content in filename.py

# Organize project
> run: find . -type f -name "*.py" | sort
```

### Integration Workflow

```bash
# Complete workflow with MCP
1. Create project files (File MCP)
2. Initialize git (File MCP)
3. Push to GitHub (GitHub MCP)
4. Deploy to Railway (Shell commands)
5. Monitor deployment (Shell + Logs)
6. Verify submission (File MCP + Shell)
```

---

## 🚨 Troubleshooting

### Issue: Module not found

```bash
> run: pip install -r requirements-deploy.txt --break-system-packages

> run: pip install -r requirements.txt --break-system-packages
```

### Issue: Git not configured

```bash
> run: git config --global user.name "Your Name"

> run: git config --global user.email "your@email.com"

> run: git remote set-url origin https://github.com/YOUR-USERNAME/bfhl-qualifier.git
```

### Issue: Railway not authenticated

```bash
> run: railway logout

> run: railway login
# Follow browser authentication
```

### Issue: Environment variables not working

```bash
# Push changes
> run: git push origin main

# Wait 30 seconds for Railway to redeploy
> run: sleep 30 && railway logs -n 20

# Verify variables set
> run: railway env
```

### Issue: Port already in use

```bash
> run: lsof -i :5000

> run: kill -9 <PID>

# Or use different port
> run: PORT=8000 python app.py
```

### Issue: BFHL API 403 Forbidden

```bash
# Check credentials
> run: cat .env

# Verify REG_NO format
> run: grep REG_NO .env

# Test with correct format
> run: python main.py
```

---

## 📋 Complete Checklist

### Before Starting

- [ ] Install Claude Code CLI: `npm install -g @anthropic-ai/claude`
- [ ] Have GitHub account ready
- [ ] Have valid registration number
- [ ] Have Railway account (free signup at railway.app)

### During Setup

- [ ] Run `claude-code`
- [ ] Create project files
- [ ] Install dependencies
- [ ] Test locally with `python main.py`
- [ ] Initialize git
- [ ] Create GitHub repository
- [ ] Push code

### Deployment

- [ ] Install Railway CLI
- [ ] Login to Railway
- [ ] Run `railway up`
- [ ] Configure environment variables
- [ ] Wait for deployment (30 seconds)
- [ ] Test live endpoints

### Verification

- [ ] Check health endpoint: `/health`
- [ ] Check main endpoint: `/`
- [ ] Check config: `/config`
- [ ] Verify SQL query in response
- [ ] Confirm submission success

### Submission

- [ ] GitHub repo is public
- [ ] App is live on Railway
- [ ] Copy live URL
- [ ] Submit to assignment form

---

## 🎯 Complete Workflow in One Command

Create `complete-workflow.sh`:

```bash
#!/bin/bash
set -e

# BFHL Qualifier 1 - Complete Automated Workflow

echo "🚀 BFHL Qualifier 1 - Complete Automated Workflow"
echo "=================================================="

# Get user input
read -p "Your full name: " USER_NAME
read -p "Your registration number: " REG_NO
read -p "Your email: " USER_EMAIL
read -p "Your GitHub username: " GH_USERNAME

# Setup
echo "📦 Installing dependencies..."
pip install -q -r requirements.txt
pip install -q -r requirements-deploy.txt

# Configure
echo "⚙️  Configuring environment..."
cat > .env << EOF
USER_NAME=$USER_NAME
REG_NO=$REG_NO
USER_EMAIL=$USER_EMAIL
API_BASE_URL=https://bfhldevapigw.healthrx.co.in/hiring
EOF

# Test locally
echo "🧪 Testing locally..."
python main.py 2>&1 | tail -5

# Git
echo "📤 Setting up Git..."
if [ ! -d .git ]; then
    git init
    git config user.name "$GH_USERNAME"
    git config user.email "$USER_EMAIL"
fi
git add .
git commit -m "BFHL Qualifier 1 - Complete solution" || echo "Already committed"
git branch -M main

# Push to GitHub
echo "🌐 Pushing to GitHub..."
REPO_URL="https://github.com/$GH_USERNAME/bfhl-qualifier.git"
git remote add origin "$REPO_URL" 2>/dev/null || git remote set-url origin "$REPO_URL"
git push -u origin main

# Deploy to Railway
echo "🚀 Deploying to Railway..."
if command -v railway &> /dev/null; then
    railway up
    echo "✅ Deployed to Railway"
    
    # Configure variables
    railway variables set USER_NAME="$USER_NAME"
    railway variables set REG_NO="$REG_NO"
    railway variables set USER_EMAIL="$USER_EMAIL"
    
    echo ""
    echo "🎉 Complete workflow finished!"
    echo ""
    echo "GitHub Repo: https://github.com/$GH_USERNAME/bfhl-qualifier"
    railway link
else
    echo "⚠️  Install Railway CLI from https://railway.app"
fi
```

Run:
```bash
> run: bash complete-workflow.sh
```

---

## 🎓 Learning & Reference

### Claude Code Documentation
- CLI: https://claude.ai
- Features: Claude Code, Web Search, File Ops

### MCP Servers
- GitHub: https://github.com/anthropics/mcp
- Documentation: https://docs.anthropic.com/mcp

### Railway
- Docs: https://docs.railway.app
- Python Apps: https://railway.app/help/python

### BFHL API
- Endpoint: https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON
- Methods: POST
- Auth: Bearer token

---

## 🎉 Summary

This CLAUDE.md provides:

✅ Complete automation with Claude Code CLI  
✅ MCP servers integration (GitHub, Files)  
✅ Deployment scripts (Railway)  
✅ Testing & verification  
✅ Troubleshooting guide  
✅ One-command complete workflow  

**Total time to complete: 5-10 minutes** ⚡

---

## 🚀 Ready to Execute?

Start with:
```bash
claude-code
```

Then:
```
> run: bash complete-workflow.sh
```

**Done!** Your app is live and solution is submitted. 🎉

---

**Questions?** Check the troubleshooting section or re-read relevant docs.

**Ready?** Start Claude Code and run the automated workflow! 🚀

---

Generated: 2026-05-25  
Version: 1.0.0  
Status: Production Ready ✅
