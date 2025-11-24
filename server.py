from http.server import SimpleHTTPRequestHandler, HTTPServer        
class MyHandler(SimpleHTTPRequestHandler)
def do_GET(self):
    if self.path == '/':
        self.path

if __name__=='__main__":
server = HTTPServer(('localhost' 8000), MyHandler)
print ("serving on localhost:8000")
sever.server_forever()
