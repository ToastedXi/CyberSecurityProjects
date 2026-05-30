# Incident Report

## Summary

Network configuration discovery activity detected on the monitored Windows endpoint.

The command `ipconfig.exe /all` was executed from a PowerShell process and captured through Wazuh process creation monitoring.

This activity is commonly associated with system and network reconnaissance.

---

## MITRE ATT&CK

| Technique ID | Technique Name                         |
| ------------ | -------------------------------------- |
| T1016        | System Network Configuration Discovery |

---

## Severity

**Low**

---

## Evidence

### Wazuh Alert Screenshot

![Wazuh Detection - ipconfig](../screenshots/threat-hunting-ipconfig.png)

*Figure 1: Wazuh detection showing execution of `ipconfig.exe /all` from a PowerShell parent process.*

### Agent

```text
WIN-Victim
```

### User

```text
Administrator
```

### Command

```text
C:\WINDOWS\system32\ipconfig.exe /all
```

### Process

```text
C:\Windows\System32\ipconfig.exe
```

### Parent Process

```text
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
```

---

## Analyst Assessment

The observed activity indicates network configuration discovery on the monitored endpoint.

The `ipconfig.exe /all` command retrieves detailed network information, including:

* IP addresses
* Network adapters
* DNS configuration
* DHCP settings
* Default gateway information
* MAC addresses

While this command is frequently executed by administrators during troubleshooting, it is also commonly used by attackers during the reconnaissance phase to understand the network environment and identify potential lateral movement opportunities.

The use of PowerShell as the parent process may warrant additional investigation if the activity was not expected.

---

## Recommended Investigation

* Verify whether the activity was performed by an authorized administrator.
* Review PowerShell activity preceding the command execution.
* Investigate for additional reconnaissance commands such as:

  * whoami.exe
  * net.exe
  * arp.exe
  * route.exe
  * nslookup.exe
* Review authentication logs for suspicious account activity.
* Determine whether additional discovery or lateral movement activity occurred.

---

## Conclusion

The activity aligns with MITRE ATT&CK technique **T1016 – System Network Configuration Discovery** and represents network reconnaissance behavior commonly observed during the discovery phase of an attack.

---

## Analyst Notes

This alert was generated during a controlled home lab exercise as part of the AI-Powered SOC Analyst project. The command was intentionally executed on a monitored Windows endpoint and detected by Wazuh through Sysmon process creation logging.
