#!/usr/bin/env python3

import requests
from utils.logger import print_log

class ProxyManager:
    def __init__(self, proxy_file=None, use_tor=False):
        self.proxies = []
        self.valid_proxies = []
        if proxy_file:
            self.load_proxies(proxy_file)
        if use_tor:
            self.add_tor_proxy()

    def load_proxies(self, file_path):
        try:
            with open(file_path, "r") as f:
                for line in f:
                    proxy = line.strip()
                    if proxy:
                        self.proxies.append(proxy)
        except Exception as e:
            print_log(f"Error loading proxies: {e}", level="error")

    def add_tor_proxy(self):
        self.proxies.append("socks5h://127.0.0.1:9050")

    def validate_proxies(self):
        for proxy in self.proxies:
            try:
                response = requests.get("https://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5)
                if response.status_code == 200:
                    self.valid_proxies.append(proxy)
            except requests.RequestException:
                continue

    def get_random_proxy(self):
        if not self.valid_proxies:
            self.validate_proxies()
        if self.valid_proxies:
            return {"http": self.valid_proxies[0], "https": self.valid_proxies[0]}
        return None

def get_proxy_manager(proxy_file=None, use_tor=False):
    return ProxyManager(proxy_file, use_tor)
