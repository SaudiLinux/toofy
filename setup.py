#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for Attack Surface Management Tool
Developer: SayerLinux
Email: SaudiLinux1@gmail.com
"""

import os
import sys
import subprocess
import platform

def install_requirements():
    """Install required Python packages"""
    print("[+] Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("[+] Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[-] Failed to install requirements: {e}")
        return False

def check_python_version():
    """Check Python version compatibility"""
    if sys.version_info < (3, 7):
        print("[-] Python 3.7 or higher is required")
        return False
    print(f"[+] Python version: {sys.version} - Compatible")
    return True

def create_directories():
    """Create necessary directories"""
    directories = [
        'templates',
        'reports',
        'logs',
        'exploits'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"[+] Created directory: {directory}")

def setup_tool():
    """Main setup function"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    Attack Surface Management Tool - Setup                    ║
║                          Developed by SayerLinux                            ║
║                        Email: SaudiLinux1@gmail.com                         ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Install requirements
    if not install_requirements():
        print("[-] Setup failed during requirements installation")
        sys.exit(1)
    
    print("\n[+] Setup completed successfully!")
    print("\n[+] Usage instructions:")
    print("1. Command line usage:")
    print("   python attack_surface_manager.py https://target.com")
    print("\n2. Web interface usage:")
    print("   python web_interface.py")
    print("   Then open: http://localhost:5000")
    print("\n[+] Important notes:")
    print("- This tool is for authorized security testing only")
    print("- Ensure you have permission before testing any target")
    print("- Review generated reports for detailed vulnerability information")
    print("\n[+] For support contact: SaudiLinux1@gmail.com")

if __name__ == "__main__":
    setup_tool()