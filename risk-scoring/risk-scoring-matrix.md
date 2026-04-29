# Hardware Security Risk Scoring Matrix
# Author: Mckintosh Mpumelelo Moyo — MS Cybersecurity, Yeshiva University
# Methodology: Likelihood x Impact = Risk Score

---

## How Risk Scores Are Calculated

Each identified threat is scored on two dimensions:

**Likelihood** — How probable is it that this threat will be exploited?
| Score | Level | Description |
|---|---|---|
| 1 | Rare | Requires nation-state level resources or physical access to a secure facility |
| 2 | Unlikely | Requires significant technical skill and specialized hardware tools |
| 3 | Possible | Exploitable by a skilled attacker with publicly available tools |
| 4 | Likely | Exploitable by a moderately skilled attacker using common tools |
| 5 | Almost Certain | Exploitable by a script kiddie or automated scanner |

**Impact** — What is the consequence if this threat is successfully exploited?
| Score | Level | Description |
|---|---|---|
| 1 | Negligible | No meaningful effect on device operation or data |
| 2 | Minor | Limited impact, easily recoverable, no data loss |
| 3 | Moderate | Partial loss of functionality or limited data exposure |
| 4 | Major | Full device compromise or significant data breach |
| 5 | Catastrophic | Complete system failure, mass data breach, or physical safety risk |

**Risk Score = Likelihood x Impact**

| Score Range | Risk Level | Action Required |
|---|---|---|
| 1 - 4 | LOW | Monitor and review annually |
| 5 - 9 | MEDIUM | Remediate within 90 days |
| 10 - 14 | HIGH | Remediate within 30 days |
| 15 - 25 | CRITICAL | Remediate immediately |

---

## Hardware Threat Risk Register

| Threat ID | Threat Description | Attack Vector | Likelihood (1-5) | Impact (1-5) | Risk Score | Risk Level | Recommended Mitigation | NIST Control |
|---|---|---|---|---|---|---|---|---|
| HW-001 | Exposed JTAG/UART debug interface in production firmware | Physical access to device ports | 4 | 5 | 20 | CRITICAL | Disable JTAG/UART in production firmware. Implement authentication if debug access is required. | PR.AA-02, PR.PS-01 |
| HW-002 | Unsigned firmware accepted by bootloader | Network or physical firmware update | 3 | 5 | 15 | CRITICAL | Implement cryptographic firmware signing. Bootloader must verify signature before execution. | PR.PS-02, PR.DS-10 |
| HW-003 | Default credentials not changed before deployment | Network or physical access | 5 | 4 | 20 | CRITICAL | Enforce unique per-device credentials generated at manufacture. Disable default accounts. | PR.AA-01, PR.PS-01 |
| HW-004 | Sensitive data stored in plaintext on flash memory | Physical access, memory dump | 3 | 4 | 12 | HIGH | Encrypt all sensitive data at rest using AES-256. Store encryption keys in secure element. | PR.DS-01 |
| HW-005 | Unencrypted network communication (HTTP, Telnet) | Network interception | 4 | 4 | 16 | CRITICAL | Disable all unencrypted protocols. Enforce TLS 1.2 minimum for all network services. | PR.DS-02 |
| HW-006 | No secure boot implementation | Physical firmware replacement | 3 | 5 | 15 | CRITICAL | Enable secure boot. Only cryptographically signed images permitted to execute. | PR.PS-05 |
| HW-007 | Counterfeit or tampered hardware components | Supply chain compromise | 2 | 5 | 10 | HIGH | Implement component verification procedures. Source from verified suppliers only. | GV.SC-06 |
| HW-008 | No firmware update mechanism | Cannot patch vulnerabilities | 4 | 4 | 16 | CRITICAL | Implement secure OTA (Over-the-Air) update mechanism with signature verification. | PR.PS-02 |
| HW-009 | Device generates no security logs | Cannot detect or investigate incidents | 4 | 3 | 12 | HIGH | Implement tamper-evident logging for auth events, config changes, and errors. | PR.PS-04, DE.CM-01 |
| HW-010 | Physical tamper protection absent | Physical access to internals | 3 | 4 | 12 | HIGH | Add tamper-evident seals. Implement active tamper detection that triggers data wipe. | PR.AA-02 |
| HW-011 | No incident response plan for hardware compromise | Delayed response to breach | 3 | 4 | 12 | HIGH | Develop hardware-specific IR playbook covering physical tampering and firmware compromise. | RS.MA-01 |
| HW-012 | Side-channel attack vulnerability (power analysis) | Physical proximity to device | 2 | 3 | 6 | MEDIUM | Implement power analysis countermeasures in hardware design. Use constant-time cryptographic operations. | PR.DS-10 |

---

## Risk Summary

| Risk Level | Count | Threats |
|---|---|---|
| CRITICAL | 5 | HW-001, HW-002, HW-003, HW-005, HW-006, HW-008 |
| HIGH | 5 | HW-004, HW-007, HW-009, HW-010, HW-011 |
| MEDIUM | 1 | HW-012 |
| LOW | 0 | — |

---

## Remediation Priority Order

1. HW-003 — Default credentials (Score: 20) — Immediate
2. HW-001 — Exposed JTAG/UART (Score: 20) — Immediate
3. HW-005 — Unencrypted communications (Score: 16) — Immediate
4. HW-008 — No firmware update mechanism (Score: 16) — Immediate
5. HW-002 — Unsigned firmware (Score: 15) — Immediate
6. HW-006 — No secure boot (Score: 15) — Immediate
7. HW-004 — Plaintext data at rest (Score: 12) — 30 days
8. HW-007 — Counterfeit components (Score: 10) — 30 days
9. HW-009 — No security logging (Score: 12) — 30 days
10. HW-010 — No tamper protection (Score: 12) — 30 days
11. HW-011 — No IR plan (Score: 12) — 30 days
12. HW-012 — Side-channel attacks (Score: 6) — 90 days