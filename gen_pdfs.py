#!/usr/bin/env python3
"""Use Chrome headless + local HTTP server to convert presentation HTML files to PDFs."""

import http.server
import os
import subprocess
import threading
import time

PORT = 8765
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FILES = ["pres-en", "pres-ru", "pres-sr"]


# Suppress server log noise
class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def log_error(self, *args):
        pass


os.chdir(BASE_DIR)
server = http.server.HTTPServer(("localhost", PORT), QuietHandler)
t = threading.Thread(target=server.serve_forever)
t.daemon = True
t.start()
time.sleep(1)
print(f"HTTP server up on port {PORT}")

for f in FILES:
    out = os.path.join(BASE_DIR, f + ".pdf")
    url = f"http://localhost:{PORT}/{f}.html"
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--print-to-pdf={out}",
        "--no-pdf-header-footer",
        "--paper-width=11.69",  # A4 landscape width in inches
        "--paper-height=8.27",  # A4 landscape height in inches
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=5000",
        url,
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
    if r.returncode == 0 and os.path.exists(out):
        size_kb = os.path.getsize(out) // 1024
        print(f"OK  {f}.pdf  ({size_kb} KB)")
    else:
        print(f"FAIL  {f}.pdf")
        if r.stderr:
            print("  stderr:", r.stderr[:300])

server.shutdown()
print("Done.")
