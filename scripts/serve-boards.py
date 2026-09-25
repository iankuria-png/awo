"""Serve Design-canvas boards locally for board-check.mjs.

Usage: python3 scripts/serve-boards.py <root> <blob dir> [port]
  <root>      folder holding project/*.dc.html and project/support.js (the canvas runtime,
              saved from the artifact's artifact-type/dc-runtime.js)
  <blob dir>  folder of uploaded images named <asset id>.<ext>, served at /_blob/<asset id>
"""
import functools
import glob
import http.server
import os
import sys

ROOT, BLOB = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
PORT = int(sys.argv[3]) if len(sys.argv) > 3 else 8792


class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        p = path.split('?')[0].split('#')[0]
        if p.startswith('/_blob/'):
            m = glob.glob(os.path.join(BLOB, p[len('/_blob/'):].strip('/') + '.*'))
            if m:
                return m[0]
        return super().translate_path(path)

    def log_message(self, fmt, *args):
        pass


http.server.ThreadingHTTPServer(('127.0.0.1', PORT), functools.partial(Handler, directory=ROOT)).serve_forever()
