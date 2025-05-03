

## Introduction

Fail2ban is an intrusion prevention software framework that protects computer servers from brute-force attacks.
It monitors log files (e.g., `/var/log/auth.log`, `/var/log/apache/access.log`) and automatically bans IP addresses that show malicious signs, such as too many password failures. 

## Prerequisites

*   Access to the Metasploitable3 command line (e.g., via SSH or the VirtualBox console).
*   Sudo privileges (the default `vagrant` user typically has this).

## Installation Steps

1.  **Log in** to your Metasploitable3 machine. 
2.  **Update Package Lists (Recommended):** 
   
    ```bash
    sudo apt-get update
    ```

3.  **Install Fail2ban:** Use the `apt-get` package manager to install Fail2ban. The first image shows the output of this command:
   
    ```bash
    sudo apt-get install fail2ban
    ```
    *   As seen in Image 1, this command fetches the `fail2ban` package and its dependencies (like `python-pyinotify` and `whois`) from the Ubuntu repositories (`us.archive.ubuntu.com`).
    *   The system confirms the required disk space and proceeds with unpacking and setting up the packages.
    *   Upon successful installation, the Fail2ban service is automatically started, indicated by the line:
        `* Starting authentication failure monitor fail2ban           [ OK ]`

## Verification

1.  **Check Service Status:** To confirm that the Fail2ban service is running correctly, use the `service` command with `sudo`:
    ```bash
    sudo service fail2ban status
    ```
2.  **Confirm Output:** As shown at the end of Image 1, the expected output for a running service is:
    ```
    * fail2ban is running
    ```

![[Pasted image 20250503220054.png]]

## Demonstration of Functionality 
![[Pasted image 20250503220117.png]]
Image 2 demonstrates the *effect* of having Fail2ban running on the target machine (Metasploitable3)

1.  **Attack Scenario:** An attacker machine (Kali Linux) uses the Metasploit Framework (`msf6`) with the `auxiliary/scanner/ssh/ssh_login` module to perform a brute-force attack against the SSH service (`port 22`) on `192.168.1.8`.
2.  **Initial Failures:** The attacker tries several username/password combinations (e.g., `root:vizxv`, `root:admin`, `admin:admin`, `root:default`), all of which fail.
3.  **Fail2ban Action:** After a configured number of failed login attempts (detected by Fail2ban monitoring the SSH authentication logs on Metasploitable3), Fail2ban automatically updates the firewall rules on Metasploitable3 to block the attacker's IP address (the Kali machine's IP).
4.  **Connection Refused:** Subsequent connection attempts from the Kali machine to the Metasploitable3 SSH service are immediately rejected, resulting in the error message:
    `[-] Could not connect: The connection was refused by the remote host (192.168.1.8:22).`

This sequence strongly indicates that Fail2ban, installed and running on Metasploitable3 as shown in Image 1, successfully detected and blocked the brute-force attack originating from the Kali machine shown in Image 2.


