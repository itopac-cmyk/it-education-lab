# Zero-Day-Lab: Professional Cyber Security Education (2026 Edition)

[![Educational Use](https://img.shields.io/badge/Purpose-Education-green)](SECURITY.md)
[![Status](https://img.shields.io/badge/Status-Seminar%20Ready-blue)](docs/SEMINAR_THREAT_MANAGEMENT.md)

## 🎯 The Seminar-Ready Lab (April 2026 Update)
This lab is a comprehensive framework for **Threat Management** and **Ethical Hacking** seminars. It covers the full spectrum from classic memory safety issues to the latest AI-driven threats.

### Advanced Seminar Modules:
1.  **[AI-Automated Exploit Generation (AEG):](docs/scenarios/SCENARIO_6_AI_AEG.md)** The future of high-speed autonomous exploitation.
2.  **[Supply Chain Attacks:](vulnerable_apps/supply_chain_lib/)** XZ Utils / Log4j style backdoor simulation.
3.  **[Identity & OAuth Exploitation:](lab_infra/auth_service/)** Bypassing perimeters via Token Theft.
4.  **[Ransomware & EDR:](docs/scenarios/SCENARIO_4_RANSOMWARE.md)** Automated encryption and eBPF-based detection.
5.  **[Hardware Side-Channels:](docs/scenarios/SCENARIO_5_HARDWARE_EXPLOITS.md)** Leakage via CPU Cache timing (Spectre/Meltdown).
6.  **[Agentic AI Prompt Injection:](docs/scenarios/SCENARIO_3_LLM_AGENT_EXPLOIT.md)** Exploiting LLMs with system access.
7.  **[Cloud-Native RCE & SSRF:](docs/scenarios/SCENARIO_2_SSRF_TO_RCE.md)** Gateway exploitation and pivoting.

---

## 🛡️ Live Threat Management Dashboard
The lab includes a **real-time SOC Dashboard** (Port 8080) that visualizes alerts from our **eBPF Kernel Monitor** and **Sigma detection rules**. 

---

## 🏗️ Lab Infrastructure
- **\`/lab_infra\`:** Docker-compose setup for the entire range.
- **\`/vulnerable_apps\`:** Source code for flawed, backdoored, and hardware-leaking apps.
- **\`/detection\`:** Kernel-level (eBPF) and SIEM-level (Sigma/YARA) detection logic.
- **\`/analysis\`:** Guides for Dynamic Analysis (GDB) and Forensics.

## 🚀 Quick Start for Instructors
1. \`cd lab_infra && docker-compose up -d\`
2. Follow the **[Seminar Guide](docs/SEMINAR_THREAT_MANAGEMENT.md)** and the **[Scenarios](docs/scenarios/)**!
