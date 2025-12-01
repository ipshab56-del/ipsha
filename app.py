from http.server import HTTPServer
from router import StudentRouter
from database.connection import init_database
def run_server(port=8000):
    # ensure DB schema exists before accepting requests
    init_database()

    server = HTTPServer(("", port), StudentRouter)
    print(f"🚀 Server running at http://localhost:{port}")
    server.serve_forever()

if __name__ == "__main__":
    run_server()