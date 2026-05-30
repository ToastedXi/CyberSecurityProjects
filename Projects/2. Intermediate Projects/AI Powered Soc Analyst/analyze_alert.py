def analyze_alert(process):
    process = process.lower()

    if "whoami.exe" in process:
        return {
            "technique": "T1033",
            "name": "System Owner/User Discovery",
            "severity": "Low",
            "summary": "User identity or privilege discovery detected."
        }

    if "net.exe" in process or "net1.exe" in process:
        return {
            "technique": "T1087.001",
            "name": "Local Account Discovery",
            "severity": "Medium",
            "summary": "Local account enumeration activity detected."
        }

    if "ipconfig.exe" in process:
        return {
            "technique": "T1016",
            "name": "System Network Configuration Discovery",
            "severity": "Low",
            "summary": "Network configuration discovery activity detected."
        }

    return {
        "technique": "Unknown",
        "name": "Unknown",
        "severity": "Unknown",
        "summary": "No ATT&CK mapping available."
    }
