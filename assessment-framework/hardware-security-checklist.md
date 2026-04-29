# Hardware Security Assessment Checklist
# Mapped to NIST CSF 2.0
# Author: Mckintosh Mpumelelo Moyo — MS Cybersecurity, Yeshiva University

---

## How to Use This Checklist

For each control, mark the status as one of:
- PASS — Control is fully implemented
- FAIL — Control is not implemented
- PARTIAL — Control is partially implemented
- N/A — Control does not apply to this device

---

## CATEGORY 1: Identity and Access Management (PR.AA)

| Control ID | Control Description | Hardware Application | Status |
|---|---|---|---|
| PR.AA-01 | Identities and credentials are managed for all hardware interfaces | Unique credentials required for each debug interface (JTAG, UART, SSH). Default credentials disabled before production. | |
| PR.AA-02 | Physical access to hardware assets is managed | Device enclosure is tamper-evident. Physical ports are disabled or locked in production units. | |
| PR.AA-03 | Hardware interfaces require authentication commensurate with risk | High-risk interfaces (JTAG, bootloader) require multi-factor or token-based authentication. | |
| PR.AA-05 | Access permissions follow least privilege principles | Service accounts and hardware interfaces only expose minimum necessary functionality. Debug features disabled in production firmware. | |

---

## CATEGORY 2: Data Security and Firmware Protection (PR.DS)

| Control ID | Control Description | Hardware Application | Status |
|---|---|---|---|
| PR.DS-01 | Data at rest is protected | Sensitive data stored on device (credentials, keys, configs) is encrypted using AES-256 or equivalent. | |
| PR.DS-02 | Data in transit is protected | All network communication from the device uses TLS 1.2 minimum. Unencrypted protocols (Telnet, HTTP) are disabled. | |
| PR.DS-10 | Data integrity is protected during processing | Firmware integrity is verified at boot using cryptographic hash validation. | |

---

## CATEGORY 3: Secure Configuration and Hardening (PR.PS)

| Control ID | Control Description | Hardware Application | Status |
|---|---|---|---|
| PR.PS-01 | Baseline secure configuration is established and maintained | A hardened firmware baseline exists. Default passwords, unnecessary services, and unused ports are disabled before production release. | |
| PR.PS-02 | Software and firmware are maintained and patched | A firmware update mechanism exists. Updates are cryptographically signed and verified before installation. | |
| PR.PS-04 | Security logs are generated and protected | Device generates tamper-evident audit logs for authentication events, configuration changes, and errors. | |
| PR.PS-05 | Installation and execution of unauthorized software is prevented | Secure boot is enabled. Only signed firmware images are permitted to execute. | |

---

## CATEGORY 4: Continuous Monitoring and Detection (DE.CM)

| Control ID | Control Description | Hardware Application | Status |
|---|---|---|---|
| DE.CM-01 | Network traffic is monitored for adverse events | Device traffic is monitored for anomalous patterns. Unexpected outbound connections trigger alerts. | |
| DE.CM-03 | Personnel activity is monitored for adverse events | Administrative access to hardware management interfaces is logged and reviewed. | |
| DE.CM-09 | Computing hardware and software are monitored | Device health metrics (CPU, memory, temperature) are monitored. Unexpected deviations trigger alerts. | |

---

## CATEGORY 5: Supply Chain and Component Security (GV.SC)

| Control ID | Control Description | Hardware Application | Status |
|---|---|---|---|
| GV.SC-03 | Suppliers and partners are assessed for risk | Hardware component suppliers are vetted for security practices. Bills of Materials (BOM) are documented and reviewed. | |
| GV.SC-06 | Supply chain risk is addressed before component acquisition | Components sourced from verified suppliers only. Counterfeit component detection procedures are in place. | |
| GV.SC-08 | Relevant suppliers are included in incident response planning | Firmware and hardware component suppliers have defined vulnerability disclosure and patching SLAs. | |

---

## CATEGORY 6: Incident Response for Hardware (RS)

| Control ID | Control Description | Hardware Application | Status |
|---|---|---|---|
| RS.MA-01 | Incident response plan is executed | A hardware-specific incident response playbook exists covering physical tampering, firmware compromise, and supply chain incidents. | |
| RS.AN-03 | Incidents are analyzed to determine root cause | Forensic analysis procedures exist for compromised hardware devices including firmware extraction and log analysis. | |
| RS.MI-01 | Incidents are contained | Compromised devices can be remotely isolated or factory reset without requiring physical access. | |

---

## Assessment Summary

| Category | Total Controls | Pass | Fail | Partial | N/A |
|---|---|---|---|---|---|
| Identity and Access Management | 4 | | | | |
| Data Security and Firmware | 3 | | | | |
| Secure Configuration | 4 | | | | |
| Continuous Monitoring | 3 | | | | |
| Supply Chain Security | 3 | | | | |
| Incident Response | 3 | | | | |
| **TOTAL** | **20** | | | | |

---

## Overall Risk Rating

| Rating | Criteria |
|---|---|
| LOW | 18-20 controls PASS |
| MEDIUM | 13-17 controls PASS |
| HIGH | 8-12 controls PASS |
| CRITICAL | 0-7 controls PASS |

**Overall Rating for This Assessment:** _______________

**Assessed By:** _______________

**Date:** _______________

**Device Assessed:** _______________