#!/usr/bin/env python3

import argparse
import sys
import os
from core.crawler import crawl_website
from core.injector import scan_injection, detect_dbms
from modules.dumper import dump_database
from modules.waf import apply_waf_bypass
from utils.logger import print_log, save_log, banner
from utils.proxy import get_proxy_manager
from utils.encoder import encode_payload

def parse_arguments():
    parser = argparse.ArgumentParser(description="BlackStackSQL - Advanced SQL Injection Automation Tool")
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

def main():
    banner()
    args = parse_arguments()

    if not args.url:
        print_log("Error: --url is required", level="error")
        sys.exit(1)

    print_log(f"Starting scan on {args.url}", level="info")

    headers = {}
    if args.user_agent:
        headers["User-Agent"] = args.user_agent
    if args.cookie:
        headers["Cookie"] = args.cookie

    proxies = None
    if args.proxy:
        proxy_manager = get_proxy_manager(args.proxy)
        proxies = proxy_manager.get_random_proxy()

    if args.resume:
        print_log(f"Resuming session from {args.resume}", level="info")
        # Implement session resume logic here

    if args.scan:
        print_log("Scanning for SQL injection vulnerabilities...", level="info")
        is_vulnerable, dbms = scan_injection(args.url, headers, args.data, args.aggressive, proxies)
        if is_vulnerable:
            print_log(f"Target is vulnerable! Detected DBMS: {dbms}", level="success")
        else:
            print_log("Target is not vulnerable.", level="warning")

    if args.dump:
        print_log("Dumping database...", level="info")
        dump_database(args.url, headers, args.data, args.columns, proxies)

    if args.output:
        save_log(args.output, f"Scan completed on {args.url}")

    if args.waf_bypass:
        print_log("WAF Bypass enabled", level="info")
        # Implement WAF bypass logic here

    print_log("Scan completed.", level="info")

if __name__ == "__main__":
    main()
