#!/usr/bin/env python3
"""Regenerate card PDFs from updated HTML files (which now contain QR codes).

Paper sizes:
  A3 landscape: 420mm x 297mm = 16.535in x 11.693in
  A6 portrait:  105mm x 148mm =  4.134in x  5.827in
"""

import http.server
import os
import subprocess
import threading
import time

PORT = 8766
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# (html_file, output_pdf, paper_width_in, paper_height_in)
CARDS = [
    ("card-EN-A6.html", "card-EN-A6.pdf", 4.134, 5.827),  # A6 portrait
    ("card-IT-A3.html", "card-IT-A3.pdf", 16.535, 11.693),  # A3 landscape
    ("card-FR-A3.html", "card-FR-A3.pdf", 16.535, 11.693),
    ("card-ES-A3.html", "card-ES-A3.pdf", 16.535, 11.693),
    ("card-SR-A3.html", "card-SR-A3.pdf", 16.535, 11.693),
    ("card-TR-A3.html", "card-TR-A3.pdf", 16.535, 11.693),
    ("card-RU-A3.html", "card-RU-A3.pdf", 16.535, 11.693),
]


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

for html, pdf, pw, ph in CARDS:
    out = os.path.join(BASE_DIR, "materials", pdf)
    url = f"http://localhost:{PORT}/materials/{html}"
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--print-to-pdf={out}",
        "--no-pdf-header-footer",
        f"--paper-width={pw}",
        f"--paper-height={ph}",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=5000",
        url,
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
    if r.returncode == 0 and os.path.exists(out):
        size_kb = os.path.getsize(out) // 1024
        print(f"OK  {pdf}  ({size_kb} KB)")
    else:
        print(f"FAIL  {pdf}")
        if r.stderr:
            print("  stderr:", r.stderr[:300])

server.shutdown()
print("Done.")
