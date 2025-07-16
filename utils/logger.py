#!/usr/bin/env python3

import os
import json
import csv
from datetime import datetime

def print_log(message, level="info"):
    levels = {
        "info": "\033[92m[+]\033[0m",
        "warning": "\033[93m[!]\033[0m",
        "error": "\033[91m[!]\033[0m",
        "success": "\033[96m[+]\033[0m"
    }
    prefix = levels.get(level, "[?]")
    print(f"{prefix} {message}")

def save_log(filename, content):
    if not os.path.exists("sessions"):
        os.makedirs("sessions")
    with open(filename, "w") as f:
        f.write(content)

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def save_csv(filename, table_data):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        for row in table_data:
            writer.writerow(row)

def banner():
    print("""
    ███████╗███████╗███████╗
    ██╔════╝██╔══██╗██╔══██╗
    █████╗  ███████║███████║
    ██╔══╝  ██╔══██║██╔══██║
    ██║     ██║  ██║██║  ██║
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝

    BlackStackSQL - Advanced SQL Injection Toolkit
    """)
