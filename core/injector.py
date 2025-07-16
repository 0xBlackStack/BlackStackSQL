#!/usr/bin/env python3

import requests
import re
import time
from utils.logger import print_log

class SQLInjector:
    def __init__(self, url, headers=None, data=None, aggressive=False):
        self.url = url
        self.headers = headers or {}
        self.data = data
        self.aggressive = aggressive
        self.payloads = self.load_payloads()

    def load_payloads(self):
        # Load payloads from files
        payloads = {
            "classic": self.read_file("payloads/classic.txt"),
            "error_based": self.read_file("payloads/error_based.txt"),
            "union_based": self.read_file("payloads/union_based.txt"),
            "time_based": self.read_file("payloads/time_based.txt"),
            "boolean_based": self.read_file("payloads/boolean_based.txt"),
        }
        return payloads

    def read_file(self, path):
        with open(path, "r") as f:
            return [line.strip() for line in f.readlines()]

    def test_payload(self, payload):
        if self.data:
            # POST request
            self.data = self.data.replace("INJECT_HERE", payload)
            response = requests.post(self.url, data=self.data, headers=self.headers)
        else:
            # GET request
            response = requests.get(self.url.replace("INJECT_HERE", payload), headers=self.headers)
        return response

    def scan_injection(self):
        for payload_type, payloads in self.payloads.items():
            for payload in payloads:
                response = self.test_payload(payload)
                if self.is_vulnerable(response):
                    print_log(f"Vulnerable to {payload_type} payload: {payload}", level="success")
                    return True, self.detect_dbms()
        print_log("No vulnerabilities found.", level="warning")
        return False, None

    def is_vulnerable(self, response):
        # Check for common SQL error messages
        error_indicators = ["sql", "syntax", "error", "warning", "unclosed quotation mark"]
        return any(indicator in response.text.lower() for indicator in error_indicators)

    def detect_dbms(self):
        # Basic DBMS detection based on error messages
        dbms_signatures = {
            "mysql": ["mysql", "mysqld", "mysql_fetch"],
            "mssql": ["microsoft", "sql server", "mssql"],
            "postgresql": ["postgresql", "pg_", "postgres"],
            "oracle": ["oracle", "pl/sql", "ora-"],
        }
        for dbms, indicators in dbms_signatures.items():
            if any(indicator in self.response.text.lower() for indicator in indicators):
                return dbms
        return "Unknown DBMS"

    def dump_database(self, columns=None):
        # Implement database dumping logic
        pass

def scan_injection(url, headers=None, data=None, aggressive=False):
    injector = SQLInjector(url, headers, data, aggressive)
    return injector.scan_injection()

def detect_dbms(url, headers=None, data=None):
    injector = SQLInjector(url, headers, data)
    return injector.detect_dbms()
