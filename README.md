
# IoT Security Monitoring with SIEM (Wazuh + ELK)

Author: Clarence  
Status: In progress  
Goal: Deploy a cloud-based SIEM lab to monitor household IoT devices and detect anomalies (unauthorized logins, unusual outbound traffic, bandwidth spikes, off-hour activity).

---

## Overview
This project demonstrates how to deploy and configure an open-source SIEM (Wazuh on the Elastic Stack) to monitor simulated IoT devices. It includes detection rules, dashboards, and documentation suitable for a professional portfolio.

## Lab Setup
- **Cloud Platform:** AWS Free Tier (EC2), Azure, or GCP
- **Virtual Machines:**
  - `Ubuntu 22.04 LTS` (SIEM server)
  - `Windows 10/11` endpoint
  - *(Optional)* lightweight Linux VM to simulate IoT traffic

## Tools & Technologies
- **SIEM:** Wazuh + Elastic Stack (ELK)
- **Traffic Simulation:** `hping3`, `nmap`, Python scripts
- **Visualization:** Kibana dashboards
- **Frameworks:** NIST CSF, MITRE ATT&CK mappings

## Detection Use Cases Implemented
1. **Failed Login Attempts** → Alert after 5+ failed SSH/RDP logins in 2 minutes.  
2. **Outbound to Suspicious IPs** → Trigger when a device connects to a known malicious IP.  
3. **Bandwidth Spike** → Detect sudden traffic surges from an IoT device.  
4. **Odd Hours Activity** → Flag unexpected device traffic between 01:00–05:00.

## Dashboards & Reports
- Failed logins over time
- Traffic by device type
- Geolocation of external connections
- Bandwidth usage alerts

*(Add screenshots to the `/screenshots` folder and link them here.)*

## Repository Structure
```
/configs       # SIEM configuration files (e.g., custom Wazuh rules)
/scripts       # Python/Bash traffic simulation scripts
/screenshots   # Dashboard images and alert examples
/reports       # PDFs or markdown reports summarizing findings
/alerts        # Sample alert payloads (JSON) or exports
README.md
LICENSE
.gitignore
```

## Results & Findings
- Detected multiple simulated IoT anomalies using custom Wazuh rules.
- Tuned alerts to reduce false positives.
- Documented workflow and incident response steps.

## Next Steps / Expansion Ideas
- Add MITRE ATT&CK mappings for each detection rule.
- Automate log collection with PowerShell/Bash agents.
- Try a cloud-native SIEM (Microsoft Sentinel) and compare.

---

## Author & Contact
- Email: cybersec.clarence.m@gmail.com  
- LinkedIn: https://www.linkedin.com/in/puresecure/
- GitHub: https://github.com/PureSecure

> If you find this useful, feel free to star the repo!
