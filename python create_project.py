import os
import subprocess
import datetime

# Set up the project structure
PROJECT_NAME = "DevOps-Pipeline-Automation"
FOLDERS = [
    ".github/workflows", "infra/terraform", "infra/ansible",
    "src/app", "k8s", "monitoring", "monitoring/grafana-dashboard",
    "logging/elk-stack"
]
FILES = {
    "README.md": "# DevOps Pipeline Automation\n\nAutomated project setup.",
    ".gitignore": "*.log\n*.pyc\n__pycache__/\n.env",
    "src/Dockerfile": "FROM python:3.9\nWORKDIR /app\nCOPY . .\nCMD ['python', 'app.py']",
    "monitoring/prometheus.yml": "global:\n  scrape_interval: 15s",
}

# Create project structure
os.makedirs(PROJECT_NAME, exist_ok=True)
for folder in FOLDERS:
    os.makedirs(os.path.join(PROJECT_NAME, folder), exist_ok=True)
for file, content in FILES.items():
    with open(os.path.join(PROJECT_NAME, file), "w") as f:
        f.write(content)

# Initialize Git
os.chdir(PROJECT_NAME)
subprocess.run(["git", "init"])
subprocess.run(["git", "branch", "-M", "main"])

# Set Git user details (update these!)
GIT_USER = "your-github-username"
GIT_REPO = "your-repo-name"
GIT_EMAIL = "your-email@example.com"

subprocess.run(["git", "config", "user.name", GIT_USER])
subprocess.run(["git", "config", "user.email", GIT_EMAIL])

# Commit files
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial commit - DevOps Project"])

# Automate 50 backdated commits
for i in range(50):
    days_ago = 100 - i  # Start from 100 days ago
    commit_date = (datetime.datetime.now() - datetime.timedelta(days=days_ago)).strftime("%Y-%m-%d %H:%M:%S")

    with open("README.md", "a") as f:
        f.write(f"\nUpdate {i+1}: Automated commit for day {days_ago}")

    subprocess.run(["git", "add", "README.md"])
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = commit_date
    env["GIT_COMMITTER_DATE"] = commit_date
    subprocess.run(["git", "commit", "-m", f"Feature Update {i+1}: Automated commit for day {days_ago}"], env=env)

# Push to GitHub
subprocess.run(["git", "remote", "add", "origin", f"https://github.com/srikanth5451/DevOps-Pipeline-Automation.git"])
subprocess.run(["git", "push", "-u", "origin", "main"])
