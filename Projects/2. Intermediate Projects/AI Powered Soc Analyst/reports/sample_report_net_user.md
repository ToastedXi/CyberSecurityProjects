# Incident Report

## Summary

Local account enumeration activity detected on the monitored Windows endpoint.

The command `net.exe user` was executed from a PowerShell process, which is commonly associated with user account discovery during reconnaissance activities.

---

## MITRE ATT&CK

| Technique ID | Technique Name          |
| ------------ | ----------------------- |
| T1087.001    | Local Account Discovery |

---

## Severity

**Medium**

---

## Evidence

### Wazuh Alert Screenshot

![Wazuh Alert - Local Account Discovery](../screenshots/threat-hunting-net-user.png)

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
C:\WINDOWS\system32\net.exe user
```

### Process

```text
C:\Windows\System32\net.exe
```

### Parent Process

```text
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
```

---

## Analyst Assessment

The observed activity indicates enumeration of local user accounts.

While this command is frequently used by administrators, it is also commonly observed during the reconnaissance phase of an attack.

The use of PowerShell as the parent process may warrant additional investigation if the activity was not expected.

---

## Recommended Investigation

* Verify whether the activity was performed by an authorized administrator.
* Review PowerShell activity preceding the command execution.
* Investigate for additional discovery commands such as:

  * whoami.exe
  * net localgroup
  * net group
  * query user
* Review authentication logs for unusual account activity.
* Determine whether additional reconnaissance or lateral movement activity occurred.

---

## Conclusion

The activity aligns with MITRE ATT&CK technique **T1087.001 – Local Account Discovery** and represents user enumeration behavior commonly observed during reconnaissance.

---

## Analyst Notes

This alert was generated during a controlled home lab exercise as part of the AI-Powered SOC Analyst project. The command was intentionally executed on a monitored Windows endpoint and detected by Wazuh through Sysmon process creation logging.
