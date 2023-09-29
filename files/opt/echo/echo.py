#!/usr/bin/env python3
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import socket

class RequestHandler(BaseHTTPRequestHandler):

    hostname = socket.gethostname()

    def respond(self, verb):
        request_path = self.path
        request_headers = self.headers
        content_length = request_headers.get('content-length')
        length = int(content_length) if content_length else 0

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        # Encode strings as bytes before writing to the response
        hostname_bytes = self.hostname.encode('utf-8')
        verb_bytes = verb.encode('utf-8')
        path_bytes = request_path.encode('utf-8')
        headers_bytes = str(request_headers).encode('utf-8')
        body_bytes = self.rfile.read(length)

        self.wfile.write(b"HOSTNAME: ")
        self.wfile.write(hostname_bytes)
        self.wfile.write(b"\nMETHOD: ")
        self.wfile.write(verb_bytes)
        self.wfile.write(b"\nURL: ")
        self.wfile.write(path_bytes)
        self.wfile.write(b"\n\nREQUEST HEADERS:\n")
        self.wfile.write(headers_bytes)
        self.wfile.write(b"\n\nREQUEST BODY:\n")
        self.wfile.write(body_bytes)
        self.wfile.write(b"\n")

    def do_GET(self):
        self.respond("GET")

    def do_POST(self):
        self.respond("POST")

    def do_PUT(self):
        self.respond("PUT")

    def do_DELETE(self):
        self.respond("DELETE")

def main():
    port = int(os.environ.get('PORT', 8080))
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('localhost', port), RequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()
