#!/usr/bin/env python3

import os
import shutil
import subprocess
import socket
import time

def print_header():
    os.system("clear")
    print("🛠  AutoFix - Linux Issue Detector\n")

def check_internet():
    print("\n[🔌] Checking Internet Connection...")
    try:
        socket.create_connection(("1.1.1.1", 53))
        print("[✅] Internet is working.")
    except:
        print("[❌] No internet connection detected!")

def check_apt_locks():
    print("\n[🛠] Checking APT Lock Issues...")
    lock_files = [
        "/var/lib/dpkg/lock",
        "/var/lib/dpkg/lock-frontend",
        "/var/cache/apt/archives/lock",
        "/var/lib/apt/lists/lock"
    ]
    found_locks = [f for f in lock_files if os.path.exists(f)]
    if found_locks:
        for lock in found_locks:
            print(f"[🔒] Lock file found: {lock}")
        print("💡 Suggestion: Run the following to remove the lock:")
        print("   sudo rm /var/lib/dpkg/lock* && sudo dpkg --configure -a")
        auto = input("⚙  Auto-fix now? (y/n): ").lower()
        if auto == "y":
            print("[⚙] Removing lock files...")
            os.system("sudo rm /var/lib/dpkg/lock*")
            os.system("sudo dpkg --configure -a")
    else:
        print("[✅] No APT lock issues.")

def check_failed_services():
    print("\n[🔍] Checking for Failed Services...")
    result = subprocess.run(["systemctl", "--failed", "--no-legend"], capture_output=True, text=True)
    output = result.stdout.strip()
    if output:
        print("[❌] Failed Services Detected:")
        print(output)
    else:
        print("[✅] No failed services.")

def check_system_usage():
    print("\n[📊] Checking System Usage...")
    os.system("top -b -n 1 | head -n 15")

def check_disk_usage():
    print("\n[💾] Disk Usage:")
    os.system("df -h | grep '^/dev/'")

def main():
    print_header()
    check_internet()
    check_apt_locks()
    check_failed_services()
    check_system_usage()
    check_disk_usage()
    print("\n✅ Scan Complete.")

if __name__ == "__main__":
    main()
