#!/usr/bin/env python3

import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="BlackStackSQL - Advanced SQL Injection Toolkit")
    parser.add_argument("--url", required=True, help="Target URL with injectable parameter")
    parser.add_argument("--data", help="POST data to inject")
    parser.add_argument("--cookie", help="Custom cookie to send")
    parser.add_argument("--user-agent", help="Custom User-Agent string")
    parser.add_argument("--proxy", help="HTTP/SOCKS proxy (e.g., 127.0.0.1:8080)")
    parser.add_argument("--scan", action="store_true", help="Perform scan only")
    parser.add_argument("--dump", action="store_true", help="Dump DB after detection")
    parser.add_argument("--columns", help="Dump specific columns (comma-separated)")
    parser.add_argument("--aggressive", action="store_true", help="Enable time-based blind & deep scan")
    parser.add_argument("--waf-bypass", action="store_true", help="Enable WAF evasion logic")
    parser.add_argument("--threads", type=int, default=5, help="Number of threads (default: 5)")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--resume", help="Resume from saved session")
    return parser.parse_args()
