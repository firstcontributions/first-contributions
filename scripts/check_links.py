#!/usr/bin/env python3
"""
Lightweight link checker for Markdown files.
Scans markdown files, extracts http(s) URLs and checks status codes.
Exits non-zero if any failing links are found.
"""
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import requests

ROOT = Path(".")
MARKDOWN_EXTS = {".md", ".markdown"}
SKIP_PREFIXES = ("mailto:", "tel:", "git://", "ssh://")
SKIP_HOSTNAMES = {"localhost", "127.0.0.1", "example.com"}
URL_RE = re.compile(r"(https?://[^\s\)\]\}>'\"]+)")

def find_markdown_files():
    for p in ROOT.rglob("*"):
        if p.is_file() and p.suffix.lower() in MARKDOWN_EXTS:
            yield p

def extract_urls(text):
    urls = set()
    # inline links [text](url)
    for m in re.finditer(r'\[.*?\]\((https?://[^\s)]+)\)', text):
        urls.add(m.group(1).rstrip(").,"))
    # reference-style [1]: url
    for m in re.finditer(r'^\s*\[[^\]]+\]:\s*(https?://\S+)', text, flags=re.MULTILINE):
        urls.add(m.group(1).rstrip(").,"))
    # plain urls
    for m in URL_RE.finditer(text):
        urls.add(m.group(1).rstrip(").,"))
    return urls

def is_skipped(url):
    if any(url.startswith(p) for p in SKIP_PREFIXES):
        return True
    parsed = urlparse(url)
    if parsed.hostname and parsed.hostname.lower() in SKIP_HOSTNAMES:
        return True
    if parsed.scheme not in ("http", "https"):
        return True
    return False

def check_url(url):
    headers = {"User-Agent": "first-contributions-link-checker/1.0"}
    try:
        # prefer HEAD to save bandwidth
        r = requests.head(url, allow_redirects=True, timeout=10, headers=headers)
        status = getattr(r, "status_code", None)
        if not isinstance(status, int) or status >= 400:
            r = requests.get(url, allow_redirects=True, timeout=10, headers=headers)
            status = getattr(r, "status_code", None)
        return status, getattr(r, "url", url)
    except requests.exceptions.RequestException as e:
        return None, str(e)

def main():
    failures = []
    total = 0
    for md in find_markdown_files():
        try:
            text = md.read_text(encoding="utf-8")
        except Exception:
            continue
        urls = extract_urls(text)
        if not urls:
            continue
        for url in urls:
            if is_skipped(url):
                continue
            total += 1
            print(f"Checking: {url} (from {md})")
            status, info = check_url(url)
            if isinstance(status, int) and 200 <= status < 400:
                pass
            else:
                failures.append((md.as_posix(), url, status, info))
                print(f"  -> FAIL: status={status} info={info}")
            time.sleep(0.2)
    if failures:
        print("\nBroken or unreachable links found:")
        for md, url, status, info in failures:
            print(f"- {md}: {url} -> status={status} info={info}")
        print(f"\nChecked {total} links, {len(failures)} failures.")
        sys.exit(2)
    else:
        print(f"All checked links OK ({total} links scanned).")
        sys.exit(0)

if __name__ == '__main__':
    main()
