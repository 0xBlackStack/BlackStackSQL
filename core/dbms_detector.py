#!/usr/bin/env python3

import requests
import re
import time
from utils.logger import print_log

class DBMSDetector:
    ERROR_SIGNATURES = {
        "mysql": [r"SQL syntax.*MySQL", r"Warning.*mysql_"],
        "mssql": [r"Unclosed quotation mark", r"Microsoft OLE DB Provider"],
        "postgresql": [r"PostgreSQL.*ERROR", r"pg_query\(\)"],
        "oracle": [r"ORA-\d{5}", r"Oracle error"],
        "sqlite": [r"SQLite3::SQLException", r"unrecognized token:"]
    }

    def __init__(self, url, method="GET", data=None, headers=None, cookies=None, proxies=None):
        self.url = url
        self.method = method
        self.data = data
        self.headers = headers or {}
        self.cookies = cookies
        self.proxies = proxies

    def detect_from_errors(self, response):
        for dbms, patterns in self.ERROR_SIGNATURES.items():
            for pattern in patterns:
                if re.search(pattern, response.text, re.IGNORECASE):
                    return {"dbms": dbms, "confidence": 0.9, "method": "error_signature", "matched": pattern}
        return None

    def detect_from_timing(self, response_time):
        if response_time > 5:
            # If response is delayed, it might be due to time-based payload
            return {"dbms": "unknown", "confidence": 0.5, "method": "time_based", "matched": "delayed_response"}
        return None

    def detect(self):
        try:
            start_time = time.time()
            if self.method.upper() == "GET":
                response = requests.get(self.url, headers=self.headers, cookies=self.cookies, proxies=self.proxies, timeout=10)
            else:
                response = requests.post(self.url, data=self.data, headers=self.headers, cookies=self.cookies, proxies=self.proxies, timeout=10)

            response_time = time.time() - start_time
            error_result = self.detect_from_errors(response)
            if error_result:
                return error_result

            timing_result = self.detect_from_timing(response_time)
            if timing_result:
                return timing_result

            return {"dbms": "unknown", "confidence": 0.1, "method": "no_match"}

        except requests.RequestException as e:
            print_log(f"Error detecting DBMS: {e}", level="error")
            return {"dbms": "unknown", "confidence": 0.0, "method": "request_error"}

def detect_dbms(url, method="GET", data=None, headers=None, cookies=None, proxies=None):
    detector = DBMSDetector(url, method, data, headers, cookies, proxies)
    return detector.detect()
