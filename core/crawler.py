#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re
from utils.logger import print_log

class WebCrawler:
    def __init__(self, base_url, max_depth=2, headers=None, cookies=None, proxies=None):
        self.base_url = base_url
        self.max_depth = max_depth
        self.headers = headers or {}
        self.cookies = cookies
        self.proxies = proxies
        self.visited = set()
        self.targets = []

    def is_valid(self, url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def get_all_forms(self, html):
        soup = BeautifulSoup(html, "html.parser")
        return soup.find_all("form")

    def get_form_details(self, form):
        details = {}
        action = form.attrs.get("action", "")
        method = form.attrs.get("method", "get").lower()
        details["action"] = urljoin(self.base_url, action)
        details["method"] = method

        inputs = []
        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            input_value = input_tag.attrs.get("value", "")
            inputs.append({"type": input_type, "name": input_name, "value": input_value})

        details["inputs"] = inputs
        return details

    def crawl(self, url, depth=0):
        if depth > self.max_depth or url in self.visited:
            return

        self.visited.add(url)
        try:
            response = requests.get(url, headers=self.headers, cookies=self.cookies, proxies=self.proxies, timeout=10)
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, "html.parser")
                for link in soup.find_all("a", href=True):
                    href = link.attrs["href"]
                    full_url = urljoin(url, href)
                    if self.is_valid(full_url) and self.base_url in full_url:
                        self.crawl(full_url, depth + 1)

                forms = self.get_all_forms(html)
                for form in forms:
                    form_details = self.get_form_details(form)
                    self.targets.append({
                        "url": form_details["action"],
                        "method": form_details["method"],
                        "params": {input["name"]: input["value"] for input in form_details["inputs"] if input["name"]},
                        "origin": "form"
                    })

                # Extract GET parameters
                if "?" in url:
                    query_params = urlparse(url).query
                    params = dict(x.split("=") for x in query_params.split("&") if "=" in x)
                    self.targets.append({
                        "url": url,
                        "method": "GET",
                        "params": params,
                        "origin": "url"
                    })

        except requests.RequestException as e:
            print_log(f"Error crawling {url}: {e}", level="error")

    def start_crawling(self):
        self.crawl(self.base_url)
        return self.targets

def crawl_website(base_url, max_depth=2, headers=None, cookies=None, proxies=None):
    crawler = WebCrawler(base_url, max_depth, headers, cookies, proxies)
    return crawler.start_crawling()
