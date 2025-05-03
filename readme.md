# SSH Attack, SIEM Analysis, and Fail2ban Defense Demonstration

## Overview

This project demonstrates a multi-phase cybersecurity exercise involving the compromise of an SSH service, analysis of the attack using a SIEM, and implementation of a defense mechanism. The goal is to showcase common attack vectors, log analysis techniques, and basic server hardening practices.

The project is divided into three phases:

1.  **Phase 1: Setup and Compromise:** Setting up attacker (Kali Linux) and victim (Metasploitable3) environments. Compromising the victim's SSH service using both Metasploit and a custom Python brute-force script.
2.  **Phase 2: Visual Analysis with SIEM:** Collecting logs from the victim machine, ingesting them into Splunk (SIEM), visualizing attack patterns (failed/successful logins, source IPs, timestamps), and correlating log data with the attacks performed in Phase 1.
3.  **Phase 3: Defense with Fail2ban:** Installing and configuring Fail2ban on the victim machine to automatically detect and block brute-force attacks by monitoring authentication logs and banning malicious IP addresses.

## Tools & Technologies Used

*   **Virtualization:** VirtualBox / UTM
*   **Attacker OS:** Kali Linux
*   **Victim OS:** Metasploitable3 (Ubuntu based)
*   **Scanning:** Nmap
*   **Exploitation Framework:** Metasploit Framework
*   **Scripting:** Python 3 (with Paramiko library)
*   **SIEM:** Splunk
*   **Intrusion Prevention:** Fail2ban
*   **Operating Systems:** macOS, Windows (for Splunk)

## Key Concepts Demonstrated

*   Service Discovery (Nmap)
*   SSH Brute-Force Attack (Metasploit, Custom Script)
*   Log Collection and Analysis
*   SIEM (Security Information and Event Management) Usage
*   Attack Pattern Visualization
*   Intrusion Detection and Prevention (Fail2ban)
*   Basic Server Hardening

## Project Phases & Contributors

*   **Phase 1: Setup and Compromise the Service**
    *   Creator: Abdulaziz (202162490)
    *   Focus: Environment setup, Nmap scanning, SSH brute-force using Metasploit and Python.

*   **Phase 2: Visual Analysis with a SIEM Dashboard**
    *   Creator: Alridha (202168410)
    *   Focus: Log collection from victim, Splunk setup, data ingestion, log visualization, and attack correlation.

*   **Phase 3: Defense Implementation with Fail2ban**
    *   Creator: Abdulrahman (202164170)
    *   Focus: Installation, configuration, and verification of Fail2ban on the victim machine to block brute-force attempts.

---

