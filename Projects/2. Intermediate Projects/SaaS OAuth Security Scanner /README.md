# 🛡️ SaaS OAuth Security Scanner

---

![Cybersecurity](https://img.shields.io/badge/CYBERSECURITY-PROJECTS-555?style=for-the-badge\&logo=github)
![Project](https://img.shields.io/badge/PROJECT-05-red?style=for-the-badge)
![Python](https://img.shields.io/badge/PYTHON-3.11+-3776AB?style=for-the-badge\&logo=python)
![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK-purple?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GITHUB-API-black?style=for-the-badge\&logo=github)
![SQLite](https://img.shields.io/badge/SQLITE-DATABASE-blue?style=for-the-badge\&logo=sqlite)
![Streamlit](https://img.shields.io/badge/STREAMLIT-DASHBOARD-red?style=for-the-badge\&logo=streamlit)
![Status](https://img.shields.io/badge/STATUS-ACTIVE-brightgreen?style=for-the-badge)

---

## 📖 Overview

**SaaS OAuth Security Scanner** is a security automation and SaaS Security Posture Management (SSPM) project designed to identify risky SaaS integrations, excessive OAuth permissions, repository security weaknesses, CI/CD attack surface exposure, and GitHub security posture issues.

The platform collects evidence from live SaaS environments, performs security analysis, generates risk findings, maps findings to MITRE ATT&CK, provides remediation guidance, stores historical assessments, and visualizes results through a modern Streamlit dashboard.

The goal of this project is to simulate the workflow of modern SSPM platforms such as:

* Microsoft Defender for Cloud Apps
* Wing Security
* Grip Security
* Nudge Security
* Obsidian Security

while demonstrating practical security engineering, automation, and risk analysis skills.

---

## 🎯 Objectives

* Collect live SaaS security data from the GitHub API
* Assess OAuth permissions and access scopes
* Identify excessive permissions
* Detect dormant SaaS integrations
* Evaluate GitHub repository exposure
* Analyze GitHub Actions workflow attack surface
* Assess branch protection posture
* Generate risk scores
* Map findings to MITRE ATT&CK
* Generate remediation guidance
* Store historical assessments
* Visualize results through a dashboard

---

## 🌎 Real World Problem

Modern organizations rely heavily on SaaS platforms such as:

* Microsoft 365
* Google Workspace
* GitHub
* Slack
* Salesforce
* Notion
* Atlassian

Employees frequently authorize third-party applications without security review.

These applications may receive permissions capable of:

* Reading email
* Sending email
* Accessing cloud storage
* Accessing source code
* Modifying CI/CD pipelines
* Maintaining persistent OAuth access

Security teams often lack visibility into:

* Which applications have access
* What permissions were granted
* Whether applications are still in use
* Which integrations create security risk

This project was created to address that visibility gap.

---

## 🏗️ Architecture

```text
GitHub API
    │
    ▼
Evidence Collection
    │
    ▼
Risk Analysis Engine
    │
    ▼
MITRE ATT&CK Mapping
    │
    ▼
Remediation Engine
    │
    ▼
SQLite Database
    │
    ▼
Historical Tracking
    │
    ▼
Executive Reporting
    │
    ▼
Streamlit Dashboard
```

---

## ⚙️ Core Features

### 🔐 OAuth Security Assessment

Analyzes SaaS applications and OAuth permissions.

Example permissions:

```text
Mail.Read
Mail.Send
Mail.ReadWrite
Files.Read.All
Files.ReadWrite.All
Directory.Read.All
offline_access
repo
workflow
admin:org
delete_repo
```

Security findings include:

* Excessive permissions
* Dormant applications
* Organization-wide admin consent
* Unknown publishers
* Broad repository access

---

### 📦 GitHub Repository Assessment

Uses the GitHub REST API to collect live repository evidence.

Analyzes:

* Public repositories
* Repository ownership
* Repository visibility
* Archived repositories
* Forked repositories
* Open issue counts

Example finding:

```text
Medium Risk

Public GitHub Repository Detected

Business Impact:
Source code exposure increases organizational attack surface.
```

---

### 🔁 GitHub Actions Workflow Assessment

Detects:

* GitHub Actions workflows
* CI/CD attack surface exposure
* Excessive workflow usage

Example finding:

```text
Medium Risk

GitHub Actions Workflow Detected

Business Impact:
Compromised workflows may expose secrets or modify deployments.
```

---

### 🌿 Branch Protection Assessment

Evaluates:

* Default branch protection
* Repository governance controls

Detects repositories where:

* Direct pushes are possible
* Pull request reviews are not enforced
* Branch protection is disabled

Example finding:

```text
High Risk

Default Branch Not Protected

Business Impact:
Attackers or accidental changes may modify production code without review.
```

---

## 🧠 MITRE ATT&CK Mapping

Findings are mapped to MITRE ATT&CK techniques including:

| Technique | Description                        |
| --------- | ---------------------------------- |
| T1078     | Valid Accounts                     |
| T1087     | Account Discovery                  |
| T1098     | Account Manipulation               |
| T1114     | Email Collection                   |
| T1213     | Data from Information Repositories |
| T1485     | Data Destruction                   |
| T1552     | Unsecured Credentials              |
| T1566     | Phishing                           |

---

## 📊 Risk Scoring Methodology

Every finding contributes to an overall risk score.

Example scoring:

| Finding                   | Points |
| ------------------------- | ------ |
| Mail.ReadWrite            | +35    |
| Admin Consent             | +15    |
| Dormant App               | +20    |
| Unknown Publisher         | +15    |
| Public Repository         | +20    |
| Missing Branch Protection | +30    |

### Risk Levels

| Score  | Rating   |
| ------ | -------- |
| 0-29   | Low      |
| 30-59  | Medium   |
| 60-79  | High     |
| 80-100 | Critical |

---

## 🔍 Evidence Collection

The scanner collects evidence directly from live SaaS environments.

Example:

```json
{
  "github_user": "ToastedXi",
  "public_repos": 7,
  "repository": "ToastedXi/MyProject",
  "workflow_count": 3
}
```

All findings are backed by evidence collected from API responses.

---

## 🗄️ Database and Historical Tracking

Assessment results are stored in SQLite.

Stored information includes:

* Assessment source
* Assessment timestamp
* Findings
* Risk scores
* Evidence

This enables:

* Historical analysis
* Security posture tracking
* Executive reporting
* Trend analysis

---

## 📈 Trend Analysis

The project supports historical assessment tracking.

Examples:

```text
GitHub Repositories
├── Assessment #1
├── Assessment #2
└── Assessment #3

Trend:
Risk Reduced 18%
```

Future versions can visualize:

* Risk reduction over time
* New findings
* Resolved findings
* Security posture improvement

---

## 📄 Reporting

The platform generates multiple reports.

### OAuth Report

```text
reports/oauth_security_report.md
```

### Repository Report

```text
reports/github_repo_report.md
```

### Workflow Report

```text
reports/github_workflow_report.md
```

### Branch Protection Report

```text
reports/github_branch_report.md
```

### Executive Report

```text
reports/executive_report.md
```

---

## 📊 Streamlit Dashboard

The project includes a modern dashboard for visualizing security posture.

### Dashboard Features

* Live scan execution
* Risk metrics
* Historical assessment tracking
* Findings explorer
* Evidence explorer
* Source filtering
* Platform filtering
* Risk filtering
* Trend visibility

### Supported Scans

* GitHub OAuth Assessment
* GitHub Repository Assessment
* GitHub Workflow Assessment
* GitHub Branch Protection Assessment

---

## 📸 Screenshots

### Dashboard Overview

![Dashboard Overview](screenshots/01-dashboard-overview.png)

### Live Scan Controls

![Live Scan Controls](screenshots/02-run-live-scans.png)

### Findings Explorer

![Findings Explorer](screenshots/03-findings-table.png)

### Evidence Viewer

![Evidence Viewer](screenshots/04-finding-detail-evidence.png)

### Repository Assessment

![Repository Assessment](screenshots/05-github-repo-report.png)

### Branch Protection Assessment

![Branch Protection Assessment](screenshots/06-github-branch-report.png)

---

## 📂 Project Structure

```text
SaaS OAuth Security Scanner/
│
├── main.py
├── dashboard.py
├── view_history.py
├── view_trends.py
├── generate_executive_report.py
│
├── scanner/
│   ├── database.py
│   ├── evidence.py
│   ├── findings.py
│   ├── mitre.py
│   ├── remediation.py
│   ├── scoring.py
│   ├── report.py
│   ├── report_repos.py
│   ├── report_workflows.py
│   ├── executive_report.py
│   ├── github_connector.py
│   ├── github_repos.py
│   ├── github_repo_risk.py
│   ├── github_workflows.py
│   ├── github_workflow_risk.py
│   ├── github_branch_protection.py
│   └── github_branch_risk.py
│
├── data/
│   ├── mock_apps.json
│   └── assessments.db
│
├── reports/
│
└── screenshots/
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/ToastedXi/CyberSecurityProjects.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔧 Environment Variables

Create a `.env` file:

```env
GITHUB_TOKEN=your_github_token_here
CLIENT_ID=
CLIENT_SECRET=
TENANT_ID=
```

---

## ▶️ Usage

### OAuth Assessment

```bash
python main.py --source github
```

### Repository Assessment

```bash
python main.py --source github-repos
```

### Workflow Assessment

```bash
python main.py --source github-workflows
```

### Branch Protection Assessment

```bash
python main.py --source github-branches
```

### View Historical Assessments

```bash
python view_history.py
```

### View Trend Summary

```bash
python view_trends.py
```

### Generate Executive Report

```bash
python generate_executive_report.py
```

### Launch Dashboard

```bash
streamlit run dashboard.py
```

---

## 🛠️ Skills Demonstrated

### Security Engineering

* SaaS Security Posture Management (SSPM)
* OAuth Security Analysis
* MITRE ATT&CK Mapping
* Risk Assessment
* Security Automation
* Security Reporting

### Development

* Python
* REST APIs
* GitHub API Integration
* Streamlit
* SQLite
* JSON Processing
* Data Analysis

### Security Operations

* Evidence Collection
* Security Dashboard Development
* Historical Assessment Tracking
* Executive Reporting
* Risk Prioritization

---

## 🔮 Future Enhancements

* Slack Integration
* Microsoft Graph Integration
* Google Workspace Integration
* PDF Executive Reports
* Secrets Detection
* Risk Trend Charts
* Finding Lifecycle Tracking
* Scheduled Scanning
* Email Alerts
* Security Scorecards

---

## ⚠️ Security Notice

This project is intended for:

* Defensive security research
* Learning and education
* Portfolio development
* Authorized security assessments

Do not use this project against systems, repositories, workspaces, or SaaS environments without explicit authorization.

---

## 👨‍💻 Author

**ToastedXi**

Cybersecurity Student | SOC Analyst | Security Automation Enthusiast

GitHub: https://github.com/ToastedXi

---

> Built to demonstrate SaaS Security Posture Management (SSPM), OAuth Security Analysis, Security Automation, Risk Assessment, MITRE ATT&CK Mapping, and Security Engineering concepts.

