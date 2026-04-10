# Zero-Day-Lab: Modern Adversary Emulation & Detection Engineering (2026 Edition)

[![Educational Use](https://img.shields.io/badge/Purpose-Education-green)](SECURITY.md)
[![Tech Stack](https://img.shields.io/badge/Tech-Docker%20%7C%20Go%20%7C%20eBPF%20%7C%20Python-blue)]()

## 🎯 Project Overview
This lab is a comprehensive framework for studying the mechanics of modern Zero-Day vulnerabilities and the latest detection engineering techniques. 

Instead of focusing purely on "how to attack," we focus on **"how to detect and mitigate."**

### Core Learning Objectives:
1.  **Vulnerability Research:** Understand modern flaws (SSTI, SSRF, AI Prompt Injection).
2.  **Adversary Emulation:** Simulating modern malware behaviors (Sleep Obfuscation) using Go.
3.  **Detection Engineering:** Writing SIEM detections (Sigma) and Kernel-level monitoring (eBPF/BCC).

---

## 🏗️ Lab Infrastructure
The lab uses Docker Compose to provide an instant, safe, and realistic enterprise environment.

### Live Scenarios (Demos):
We have built dedicated, containerized microservices to simulate the exact mechanics of the most devastating recent attacks, plus a look into the future:

1.  **[Scenario 1: Cloud-Native RCE (SSTI/Deserialization)](docs/SCENARIO_1_SSTI_TO_RCE.md)**
2.  **[Scenario 2: Gateway SSRF to Internal RCE (Simulating Ivanti/ProxyNotShell mechanics)](docs/scenarios/SCENARIO_2_SSRF_TO_RCE.md)**
3.  **[Scenario 3: Future Zero-Days - AI Agent Prompt Injection to RCE](docs/scenarios/SCENARIO_3_LLM_AGENT_EXPLOIT.md)**

---

## 🚀 Quick Start
1. Read the [Security & Ethics Policy](SECURITY.md).
2. Start the lab: `cd lab_infra && docker-compose up -d`
3. Enter the attacker node: `docker-compose exec attacker_node bash`
4. Follow the Scenario guides in the `/docs` folder!

## 🎓 Academic Context
Designed for students and researchers to master the technical depth of **Offensive Security** within an ethical framework (M.Sc. Cyber Security).
