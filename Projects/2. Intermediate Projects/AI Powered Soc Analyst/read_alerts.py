import json
from analyze_alert import analyze_alert
from report_generator import generate_report

alerts_file = "/var/ossec/logs/alerts/alerts.json"

interesting_processes = [
    "powershell.exe",
    "cmd.exe",
    "whoami.exe",
    "net.exe",
    "net1.exe",
    "ipconfig.exe"
]

with open(alerts_file, "r") as f:
    for line in f:
        try:
            alert = json.loads(line)

            agent = alert.get("agent", {}).get("name")
            rule = alert.get("rule", {}).get("description")
            level = alert.get("rule", {}).get("level")

            if agent != "WIN-Victim":
                continue

            data = alert.get("data", {}).get("win", {}).get("eventdata", {})

            command = data.get("commandLine")
            process = data.get("newProcessName")
            parent = data.get("parentProcessName")
            user = data.get("subjectUserName")

            if not process:
                continue

            if not any(proc.lower() in process.lower() for proc in interesting_processes):
                continue

            analysis = analyze_alert(process)

            if analysis["technique"] == "Unknown":
                continue

            alert_data = {
                "agent": agent,
                "rule": rule,
                "level": level,
                "user": user,
                "command": command,
                "process": process,
                "parent": parent
            }

            print("=" * 60)
            print("Agent:", agent)
            print("Rule:", rule)
            print("Level:", level)
            print("User:", user)
            print("Command:", command)
            print("Process:", process)
            print("Parent:", parent)
            print()
            print("MITRE ATT&CK:", analysis["technique"])
            print("Technique:", analysis["name"])
            print("Severity:", analysis["severity"])
            print("Summary:", analysis["summary"])

            report = generate_report(alert_data, analysis)
            print(report)

        except Exception:
            pass
