from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Handle incoming HTTP GET requests
    def do_GET(self):
        # Send a 200 OK response status
        self.send_response(200)
        
        # Set the content type header to HTML
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Write the body of the response (must be encoded to bytes)
        self.wfile.write(b"<h1>Hello, World! This is a simple Python web server.</h1>")

def run():
    server_address = ('', 8000) # Listens on all available interfaces at port 8000
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server running on http://localhost:8000...")
    
    try:
        httpd.serve_forever() # Keeps the server running indefinitely
    except KeyboardInterrupt:
        print("\nServer stopping...")
        httpd.server_close()

if __name__ == "__main__":
    run()