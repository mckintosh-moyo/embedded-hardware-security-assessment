# Embedded Hardware Security Assessment Framework

A structured GRC assessment toolkit for evaluating security controls on embedded hardware platforms, mapped to NIST CSF 2.0 and ISO 27001.

Built by Mckintosh Mpumelelo Moyo — MS Cybersecurity, Yeshiva University

---

## What This Project Is
## 📽️ Project Demo

![Hardware Security Risk Assessment Demo](demo.gif)

This framework helps security analysts and GRC teams assess the security posture of embedded hardware products — such as smart building controllers, IoT devices, and industrial systems. It covers the full assessment lifecycle from initial scoping to risk scoring to remediation reporting.

This project was built to reflect real-world GRC workflows used in hardware security teams, specifically aligned to the responsibilities of an Information Security Analyst supporting embedded platform security.

---

## Repository Structure

| Folder | Contents |
|---|---|
| `assessment-framework/` | Hardware security assessment checklists mapped to NIST CSF 2.0 |
| `risk-scoring/` | Risk scoring matrix (Likelihood x Impact) for hardware threats |
| `sample-report/` | A completed sample assessment report for a fictional embedded device |
| `policies/` | Security policy templates for embedded hardware platforms |

---

## Frameworks Used

- NIST Cybersecurity Framework (CSF) 2.0
- ISO/IEC 27001:2022
- NIST SP 800-82 (Guide to ICS/OT Security)
- OWASP Embedded Application Security

---

## Hardware Threat Categories Covered

- Firmware tampering and unsigned firmware
- JTAG/UART debug interface exposure
- Physical access and hardware reverse engineering
- Supply chain integrity
- Insecure boot process
- Side-channel attacks
- Network-level attacks on embedded services

---

## How I Would Use This at Crestron

Crestron builds embedded hardware products for smart buildings and automation systems. This framework directly supports the GRC activities described in Crestron's InfoSec Co-Op role — specifically security assessments of hardware products, vulnerability triage, policy development, and remediation planning for embedded platforms.

---

## Author

**Mckintosh Mpumelelo Moyo**
MS Cybersecurity — Yeshiva University, Katz School of Science and Health
[LinkedIn](https://www.linkedin.com/in/mckintosh-moyo)