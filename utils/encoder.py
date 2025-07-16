#!/usr/bin/env python3

import random
import urllib.parse
import binascii

class PayloadEncoder:
    def __init__(self, payload):
        self.payload = payload

    def inline_comments(self):
        return "".join([c + "/*" + c + "*/" for c in self.payload])

    def random_case(self):
        return "".join(random.choice([c.upper(), c.lower()]) for c in self.payload)

    def unicode_encode(self):
        return "".join(f"\\u{ord(c):04x}" for c in self.payload)

    def hex_encode(self):
        return "".join(f"\\x{binascii.hexlify(c.encode()).decode()}" for c in self.payload)

    def url_encode(self):
        return urllib.parse.quote(self.payload)

    def double_url_encode(self):
        return urllib.parse.quote(urllib.parse.quote(self.payload))

    def encode(self, method="all"):
        if method == "all":
            return {
                "original": self.payload,
                "commented": self.inline_comments(),
                "random_case": self.random_case(),
                "unicode": self.unicode_encode(),
                "hex": self.hex_encode(),
                "url_encoded": self.url_encode(),
                "double_url_encoded": self.double_url_encode()
            }
        elif method == "commented":
            return self.inline_comments()
        elif method == "random_case":
            return self.random_case()
        elif method == "unicode":
            return self.unicode_encode()
        elif method == "hex":
            return self.hex_encode()
        elif method == "url_encoded":
            return self.url_encode()
        elif method == "double_url_encoded":
            return self.double_url_encode()
        else:
            return self.payload

def encode_payload(payload, method="all"):
    encoder = PayloadEncoder(payload)
    return encoder.encode(method)
