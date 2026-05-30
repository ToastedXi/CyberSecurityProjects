def generate_report(alert, analysis):
    report = f"""
# Incident Report

## Summary
{analysis['summary']}

## MITRE ATT&CK
Technique ID: {analysis['technique']}
Technique Name: {analysis['name']}

## Severity
{analysis['severity']}

## Evidence
Agent: {alert['agent']}
Rule: {alert['rule']}
Rule Level: {alert['level']}
User: {alert['user']}

Command:
{alert['command']}

Process:
{alert['process']}

Parent Process:
{alert['parent']}

## Recommended Investigation
- Confirm whether this activity was expected.
- Review surrounding process creation events.
- Check what user account executed the command.
- Look for follow-on discovery, credential access, or lateral movement activity.
"""

    return report

