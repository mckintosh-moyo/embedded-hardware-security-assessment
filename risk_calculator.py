# Hardware Security Risk Score Calculator
# Author: Mckintosh Mpumelelo Moyo — MS Cybersecurity, Yeshiva University
# Description: Reads a CSV of hardware threats and generates a prioritized
#              risk report as an HTML file.

import csv
import datetime

# ── Risk data: each threat has a name, likelihood, impact, mitigation, and NIST control
threats = [
    {
        "id": "HW-001",
        "threat": "Exposed JTAG/UART debug interface",
        "likelihood": 4,
        "impact": 5,
        "mitigation": "Disable JTAG/UART in production firmware",
        "nist_control": "PR.AA-02, PR.PS-01"
    },
    {
        "id": "HW-002",
        "threat": "Unsigned firmware accepted by bootloader",
        "likelihood": 3,
        "impact": 5,
        "mitigation": "Implement cryptographic firmware signing",
        "nist_control": "PR.PS-02, PR.DS-10"
    },
    {
        "id": "HW-003",
        "threat": "Default credentials not changed before deployment",
        "likelihood": 5,
        "impact": 4,
        "mitigation": "Enforce unique per-device credentials at manufacture",
        "nist_control": "PR.AA-01, PR.PS-01"
    },
    {
        "id": "HW-004",
        "threat": "Sensitive data stored in plaintext on flash memory",
        "likelihood": 3,
        "impact": 4,
        "mitigation": "Encrypt all sensitive data at rest using AES-256",
        "nist_control": "PR.DS-01"
    },
    {
        "id": "HW-005",
        "threat": "Unencrypted network communication (HTTP, Telnet)",
        "likelihood": 4,
        "impact": 4,
        "mitigation": "Disable unencrypted protocols. Enforce TLS 1.2 minimum",
        "nist_control": "PR.DS-02"
    },
    {
        "id": "HW-006",
        "threat": "No secure boot implementation",
        "likelihood": 3,
        "impact": 5,
        "mitigation": "Enable secure boot with cryptographic chain of trust",
        "nist_control": "PR.PS-05"
    },
    {
        "id": "HW-007",
        "threat": "Counterfeit or tampered hardware components",
        "likelihood": 2,
        "impact": 5,
        "mitigation": "Implement component verification and approved vendor list",
        "nist_control": "GV.SC-06"
    },
    {
        "id": "HW-008",
        "threat": "No firmware update mechanism",
        "likelihood": 4,
        "impact": 4,
        "mitigation": "Implement secure OTA update with signature verification",
        "nist_control": "PR.PS-02"
    },
    {
        "id": "HW-009",
        "threat": "Device generates no security logs",
        "likelihood": 4,
        "impact": 3,
        "mitigation": "Implement tamper-evident logging for auth and config events",
        "nist_control": "PR.PS-04, DE.CM-01"
    },
    {
        "id": "HW-010",
        "threat": "Physical tamper protection absent",
        "likelihood": 3,
        "impact": 4,
        "mitigation": "Add tamper-evident seals and active tamper detection",
        "nist_control": "PR.AA-02"
    },
    {
        "id": "HW-011",
        "threat": "No incident response plan for hardware compromise",
        "likelihood": 3,
        "impact": 4,
        "mitigation": "Develop hardware-specific IR playbook",
        "nist_control": "RS.MA-01"
    },
    {
        "id": "HW-012",
        "threat": "Side-channel attack vulnerability",
        "likelihood": 2,
        "impact": 3,
        "mitigation": "Implement power analysis countermeasures in hardware design",
        "nist_control": "PR.DS-10"
    },
]

# ── Calculate risk scores
def get_risk_level(score):
    if score >= 15:
        return "CRITICAL"
    elif score >= 10:
        return "HIGH"
    elif score >= 5:
        return "MEDIUM"
    else:
        return "LOW"

def get_risk_color(level):
    colors = {
        "CRITICAL": "#ff4444",
        "HIGH":     "#ff8800",
        "MEDIUM":   "#ffcc00",
        "LOW":      "#44bb44"
    }
    return colors.get(level, "#ffffff")

def get_timeline(level):
    timelines = {
        "CRITICAL": "Immediate",
        "HIGH":     "Within 30 days",
        "MEDIUM":   "Within 90 days",
        "LOW":      "Annual review"
    }
    return timelines.get(level, "TBD")

# ── Score all threats
for threat in threats:
    threat["score"] = threat["likelihood"] * threat["impact"]
    threat["risk_level"] = get_risk_level(threat["score"])
    threat["color"] = get_risk_color(threat["risk_level"])
    threat["timeline"] = get_timeline(threat["risk_level"])

# ── Sort by risk score descending
threats_sorted = sorted(threats, key=lambda x: x["score"], reverse=True)

# ── Count by risk level
counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
for t in threats:
    counts[t["risk_level"]] += 1

# ── Generate HTML report
date_str = datetime.datetime.now().strftime("%B %d, %Y")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hardware Security Risk Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background: #f5f5f5;
            color: #333;
        }}
        h1 {{
            color: #1B3A6B;
            border-bottom: 3px solid #1B3A6B;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #2E75B6;
            margin-top: 30px;
        }}
        .meta {{
            background: #1B3A6B;
            color: white;
            padding: 15px 20px;
            border-radius: 6px;
            margin-bottom: 25px;
        }}
        .meta p {{ margin: 4px 0; }}
        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin-bottom: 30px;
        }}
        .summary-card {{
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            color: white;
            font-weight: bold;
        }}
        .summary-card .number {{
            font-size: 2.5em;
            display: block;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        th {{
            background: #1B3A6B;
            color: white;
            padding: 12px 15px;
            text-align: left;
            font-size: 0.9em;
        }}
        td {{
            padding: 11px 15px;
            border-bottom: 1px solid #eee;
            font-size: 0.88em;
        }}
        tr:last-child td {{ border-bottom: none; }}
        tr:hover td {{ background: #f9f9f9; }}
        .badge {{
            padding: 4px 10px;
            border-radius: 12px;
            color: white;
            font-weight: bold;
            font-size: 0.82em;
            display: inline-block;
        }}
        .footer {{
            margin-top: 40px;
            text-align: center;
            color: #888;
            font-size: 0.85em;
            border-top: 1px solid #ddd;
            padding-top: 15px;
        }}
    </style>
</head>
<body>
    <h1>Hardware Security Risk Assessment Report</h1>

    <div class="meta">
        <p><strong>Author:</strong> Mckintosh Mpumelelo Moyo</p>
        <p><strong>Program:</strong> MS Cybersecurity — Yeshiva University, Katz School</p>
        <p><strong>Framework:</strong> NIST CSF 2.0</p>
        <p><strong>Generated:</strong> {date_str}</p>
    </div>

    <h2>Risk Summary</h2>
    <div class="summary-grid">
        <div class="summary-card" style="background:#ff4444;">
            <span class="number">{counts['CRITICAL']}</span>
            CRITICAL
        </div>
        <div class="summary-card" style="background:#ff8800;">
            <span class="number">{counts['HIGH']}</span>
            HIGH
        </div>
        <div class="summary-card" style="background:#ccaa00;">
            <span class="number">{counts['MEDIUM']}</span>
            MEDIUM
        </div>
        <div class="summary-card" style="background:#44bb44;">
            <span class="number">{counts['LOW']}</span>
            LOW
        </div>
    </div>

    <h2>Prioritized Threat Register</h2>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Threat</th>
                <th>Likelihood</th>
                <th>Impact</th>
                <th>Score</th>
                <th>Risk Level</th>
                <th>NIST Control</th>
                <th>Timeline</th>
                <th>Mitigation</th>
            </tr>
        </thead>
        <tbody>
"""

for t in threats_sorted:
    html += f"""
            <tr>
                <td><strong>{t['id']}</strong></td>
                <td>{t['threat']}</td>
                <td style="text-align:center">{t['likelihood']}</td>
                <td style="text-align:center">{t['impact']}</td>
                <td style="text-align:center"><strong>{t['score']}</strong></td>
                <td><span class="badge" style="background:{t['color']}">{t['risk_level']}</span></td>
                <td style="font-size:0.82em">{t['nist_control']}</td>
                <td>{t['timeline']}</td>
                <td style="font-size:0.82em">{t['mitigation']}</td>
            </tr>
"""

html += """
        </tbody>
    </table>

    <div class="footer">
        <p>Generated by Hardware Security Risk Score Calculator</p>
        <p>Mckintosh Mpumelelo Moyo — MS Cybersecurity, Yeshiva University</p>
        <p>Framework: NIST CSF 2.0 | For educational and professional use</p>
    </div>
</body>
</html>
"""

# ── Write HTML report to file
output_file = "risk-scoring/risk-report.html"
with open(output_file, "w") as f:
    f.write(html)

print("=" * 55)
print("  Hardware Security Risk Report — Generated!")
print("=" * 55)
print(f"  Date:          {date_str}")
print(f"  Total Threats: {len(threats)}")
print(f"  CRITICAL:      {counts['CRITICAL']}")
print(f"  HIGH:          {counts['HIGH']}")
print(f"  MEDIUM:        {counts['MEDIUM']}")
print(f"  LOW:           {counts['LOW']}")
print("=" * 55)
print(f"  Report saved to: {output_file}")
print("=" * 55)