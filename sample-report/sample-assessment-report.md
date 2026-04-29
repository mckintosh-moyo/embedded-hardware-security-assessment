# Hardware Security Assessment Report
# Device: Crestron-Style Smart Building Controller (Fictional)
# Author: Mckintosh Mpumelelo Moyo — MS Cybersecurity, Yeshiva University
# Date: April 2026
# Classification: SAMPLE / EDUCATIONAL USE ONLY

---

## 1. Executive Summary

This report presents the findings of a hardware security assessment conducted
on a fictional smart building automation controller — a device representative
of the embedded systems used in commercial building management for audio
visual control, lighting, HVAC, and access control integration.

The assessment evaluated 20 security controls across six categories mapped
to NIST CSF 2.0. Of the 20 controls assessed, 5 were rated PASS, 8 were
rated PARTIAL, and 7 were rated FAIL. The overall risk rating is HIGH.

Immediate remediation is required for three critical findings: exposed debug
interfaces, unsigned firmware acceptance, and default credentials shipped
in production units.

---

## 2. Device Overview

| Field | Details |
|---|---|
| Device Name | SBC-4000 Smart Building Controller (Fictional) |
| Manufacturer | MediBuild Systems (Fictional) |
| Firmware Version | v2.3.1 |
| Operating System | Embedded Linux (BusyBox) |
| Network Interfaces | Ethernet (RJ45), Wi-Fi 802.11ac |
| Physical Interfaces | JTAG, UART, USB-A x2, SD Card slot |
| Primary Function | Building automation — AV, lighting, HVAC, access control |
| Assessment Date | April 2026 |
| Assessed By | Mckintosh Mpumelelo Moyo |

---

## 3. Assessment Scope

This assessment covered the following attack surfaces:

- Firmware security and update mechanism
- Physical debug interface exposure (JTAG, UART)
- Network communication security
- Credential and authentication management
- Data protection at rest and in transit
- Supply chain component integrity
- Logging and monitoring capability
- Incident response readiness

---

## 4. Assessment Findings

### 4.1 Identity and Access Management

| Control ID | Control | Status | Finding |
|---|---|---|---|
| PR.AA-01 | Credential management for hardware interfaces | FAIL | Device ships with default username: admin / password: admin123. No mechanism forces credential change on first boot. |
| PR.AA-02 | Physical access management | PARTIAL | Device enclosure has basic screws but no tamper-evident seals. JTAG and UART ports are physically accessible. |
| PR.AA-03 | Authentication commensurate with risk | FAIL | JTAG interface has no authentication. Full read/write access to firmware is available to anyone with physical access and a JTAG debugger. |
| PR.AA-05 | Least privilege principles | PARTIAL | Network services run as root. No service account separation exists between AV, lighting, and HVAC control functions. |

### 4.2 Data Security and Firmware Protection

| Control ID | Control | Status | Finding |
|---|---|---|---|
| PR.DS-01 | Data at rest protection | FAIL | Wi-Fi credentials, API keys, and building access codes stored in plaintext in /etc/config on the device filesystem. |
| PR.DS-02 | Data in transit protection | PARTIAL | HTTPS is used for cloud communication but local API endpoints between building subsystems use unencrypted HTTP on port 80. |
| PR.DS-10 | Data integrity during processing | FAIL | No cryptographic hash verification of firmware at boot. Any firmware image is accepted by the bootloader without validation. |

### 4.3 Secure Configuration and Hardening

| Control ID | Control | Status | Finding |
|---|---|---|---|
| PR.PS-01 | Baseline secure configuration | FAIL | Telnet service enabled by default on port 23. SSH available but not enforced. Unnecessary services (FTP, SNMP v1) running. |
| PR.PS-02 | Software and firmware maintenance | PARTIAL | Firmware update mechanism exists but updates are not cryptographically signed. Any firmware image with correct file extension is accepted. |
| PR.PS-04 | Security logs generated | PARTIAL | System logs exist in /var/log but cover only system errors. Authentication events and configuration changes are not logged. |
| PR.PS-05 | Unauthorized software prevention | FAIL | Secure boot not implemented. No restriction on executing unsigned code. |

### 4.4 Continuous Monitoring and Detection

| Control ID | Control | Status | Finding |
|---|---|---|---|
| DE.CM-01 | Network traffic monitoring | FAIL | No network monitoring capability on device. No alerts for unexpected outbound connections. |
| DE.CM-03 | Personnel activity monitoring | FAIL | Administrative access to management interface generates no audit log entries. |
| DE.CM-09 | Hardware health monitoring | PASS | Device reports CPU, memory, and temperature metrics to cloud dashboard every 60 seconds. |

### 4.5 Supply Chain and Component Security

| Control ID | Control | Status | Finding |
|---|---|---|---|
| GV.SC-03 | Supplier risk assessment | PARTIAL | Primary component suppliers are documented but no formal security assessment of suppliers has been conducted. |
| GV.SC-06 | Supply chain risk before acquisition | PASS | Components sourced from approved vendor list. No counterfeit detection procedures in place however. |
| GV.SC-08 | Suppliers in incident response | FAIL | No SLA exists with firmware or hardware suppliers for vulnerability disclosure or emergency patching. |

### 4.6 Incident Response

| Control ID | Control | Status | Finding |
|---|---|---|---|
| RS.MA-01 | Incident response plan execution | FAIL | No hardware-specific incident response plan exists. General IT IR plan does not cover physical tampering or firmware compromise scenarios. |
| RS.AN-03 | Incident analysis and root cause | PARTIAL | Basic system logs exist but are insufficient for forensic analysis of a hardware compromise event. |
| RS.MI-01 | Incident containment | PASS | Device supports remote factory reset via cloud management portal. |

---

## 5. Risk Summary

| Category | Total | PASS | PARTIAL | FAIL |
|---|---|---|---|---|
| Identity and Access Management | 4 | 0 | 2 | 2 |
| Data Security and Firmware | 3 | 0 | 1 | 2 |
| Secure Configuration | 4 | 0 | 2 | 2 |
| Continuous Monitoring | 3 | 1 | 0 | 2 |
| Supply Chain Security | 3 | 1 | 1 | 1 |
| Incident Response | 3 | 1 | 1 | 1 |
| **T