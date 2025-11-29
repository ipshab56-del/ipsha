"""Minimal server entrypoint kept for backward compatibility.

This file provides a simple HTTP server using the application's router
handler. Use `app.py` directly to run the server or run this file.
"""

from http.server import HTTPServer
from router import StudentRouter


def run_server(host: str = "localhost", port: int = 8000):
    server = HTTPServer((host, port), StudentRouter)
    print(f"serving on {host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
