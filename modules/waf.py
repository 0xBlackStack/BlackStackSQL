#!/usr/bin/env python3

import random
import urllib.parse

def apply_waf_bypass(payload, method="random_case"):
    if method == "random_case":
        return random_case(payload)
    elif method == "inline_comments":
        return inline_comments(payload)
    elif method == "url_encoding":
        return url_encoding(payload)
    elif method == "hex_encoding":
        return hex_encoding(payload)
    elif method == "combo":
        return combo(payload)
    else:
        return payload

def random_case(payload):
    return "".join(random.choice([c.upper(), c.lower()]) for c in payload)

def inline_comments(payload):
    return "".join([c + "/*" + c + "*/" for c in payload])

def url_encoding(payload):
    return urllib.parse.quote(payload)

def hex_encoding(payload):
    return "".join(f"\\x{ord(c):02x}" for c in payload)

def combo(payload):
    return random_case(inline_comments(payload))
