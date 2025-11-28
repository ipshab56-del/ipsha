# Matches incoming HTTP paths (URLs) to handlers (like a tiny Express/Django router)

from datetime import datetime
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

from controller.student import (
    get_all_students
    
)

from core.static import serve_static
from core.response import send_404
from core.middleware import add_cors_headers


class StudentRouter(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
       
        self.send_response(200)
        add_cors_headers(self)
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path


      
        if path == "/api/students":
            return get_all_students(self)

        return send_404(self)

    
    def log_message(self, format, *args):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [Server] {format % args}")