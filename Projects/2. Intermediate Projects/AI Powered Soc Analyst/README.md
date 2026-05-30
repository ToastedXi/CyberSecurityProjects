# 🛡️ AI-Powered SOC Analyst

![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Projects-black?style=for-the-badge&logo=github)
![Project](https://img.shields.io/badge/Project-04-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.14+-blue?style=for-the-badge&logo=python)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-purple?style=for-the-badge)
![Wazuh](https://img.shields.io/badge/Wazuh-SIEM-blue?style=for-the-badge)
![Security Operations](https://img.shields.io/badge/SOC-Automation-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

## 📖 Overview

AI Powered SOC Analyst is a Security Operations (SOC) automation project that ingests endpoint telemetry from Wazuh, analyzes security events, maps activity to the MITRE ATT&CK framework, and automatically generates incident reports.

The goal of the project is to simulate the workflow of a real SOC analyst by automating alert triage, enrichment, and reporting.

---

## 🎯 Objectives

- Collect endpoint telemetry from Windows systems
- Detect suspicious process activity
- Parse Wazuh alerts automatically
- Map events to MITRE ATT&CK techniques
- Generate analyst-friendly incident reports
- Prepare the foundation for AI-powered alert analysis

---

## 🏗️ Architecture

```text
Windows 11 Endpoint
        │
        ▼
   Wazuh Agent
        │
        ▼
   Wazuh Manager
        │
        ▼
   alerts.json
        │
        ▼
 Python Alert Parser
        │
        ▼
 MITRE ATT&CK Mapping
        │
        ▼
 Incident Report Generator
        │
        ▼
 SOC Analyst Output
```

---

## 🖥️ Lab Environment

### Victim Machine

- Windows 11 Enterprise
- Wazuh Agent

### SIEM Server

- Ubuntu Server
- Wazuh Manager
- Wazuh Dashboard

### Attacker Machine

- Kali Linux

---

## ⚙️ Features

### Alert Parsing

Parses Wazuh alerts directly from:

```text
/var/ossec/logs/alerts/alerts.json
```

Extracts:

- Agent Name
- User
- Command Line
- Process Name
- Parent Process
- Rule Description
- Severity Level

---

### MITRE ATT&CK Mapping

Current mappings include:

| Command | Technique | Description |
|----------|----------|----------|
| whoami.exe | T1033 | System Owner/User Discovery |
| net.exe user | T1087.001 | Local Account Discovery |
| net1.exe user | T1087.001 | Local Account Discovery |
| ipconfig.exe | T1016 | System Network Configuration Discovery |

---

### Incident Report Generation

Example output:

```text
# Incident Report

Summary:
Network configuration discovery activity detected.

MITRE ATT&CK:
T1016 - System Network Configuration Discovery

Severity:
Low

Evidence:
ipconfig.exe /all

Recommended Investigation:
- Review surrounding activity
- Verify user intent
- Investigate follow-on discovery commands
```

---

## 📂 Project Structure

```text
ai-soc-analyst/
│
├── analyze_alert.py
├── read_alerts.py
├── report_generator.py
│
├── reports/
│   ├── report_001.md
│   ├── report_002.md
│
└── README.md
```

---

## 🚀 Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-powered-soc-analyst.git

cd ai-powered-soc-analyst
```

Create virtual environment:

```bash
python3 -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install pandas
```

Run:

```bash
python3 read_alerts.py
```

---

## 🔍 Example Detection

### Command Executed

```powershell
net user
```

### Event Observed

```text
Parent Process:
powershell.exe

Child Process:
net.exe
```

### MITRE Mapping

```text
T1087.001
Local Account Discovery
```

### Analyst Assessment

```text
Account enumeration activity detected.

An attacker may be attempting to identify local user accounts
for privilege escalation or lateral movement.
```

---

## 📈 Future Enhancements

### Phase 2

- OpenAI Integration
- Ollama Integration
- LLM-Powered Alert Analysis
- Dynamic MITRE Mapping
- Investigation Recommendations
- Executive Summaries

### Phase 3

- Web Dashboard
- Alert Scoring
- Risk Prioritization
- Threat Intelligence Enrichment
- Multi-Host Correlation

---

## 🛠️ Technologies Used

- Python
- Wazuh
- Windows Event Logging
- Ubuntu Server
- Kali Linux
- MITRE ATT&CK Framework

---

## 📚 Skills Demonstrated

### Security Operations

- Threat Hunting
- Alert Triage
- Incident Investigation
- Security Monitoring

### Detection Engineering

- Event Analysis
- Process Monitoring
- ATT&CK Mapping

### Automation

- Python Scripting
- Log Parsing
- Report Generation

### Security Architecture

- SIEM Deployment
- Endpoint Telemetry
- SOC Workflows

---

## 📄 License

AGPL v3

---

## 👤 Author

Built as part of a Cyber Security Home Lab and Detection Engineering portfolio project.
