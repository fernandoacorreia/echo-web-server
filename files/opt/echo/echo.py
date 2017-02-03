#!/usr/bin/env python
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import socket

class RequestHandler(BaseHTTPRequestHandler):

    hostname = socket.gethostname()

    def respond(self, verb):
        request_path = self.path
        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write("HOSTNAME: %s\n" % (self.hostname))
        self.wfile.write("METHOD: %s\n" % (verb))
        self.wfile.write("URL: %s\n" % (request_path))
        self.wfile.write("\n")
        self.wfile.write("REQUEST HEADERS:")
        self.wfile.write("\n")
        self.wfile.write(request_headers)
        self.wfile.write("\n")
        self.wfile.write("REQUEST BODY:")
        self.wfile.write("\n")
        self.wfile.write(self.rfile.read(length))
        self.wfile.write("\n")

    def do_GET(self):
        self.respond("GET")

    def do_POST(self):
        self.respond("POST")

    def do_PUT(self):
        self.respond("PUT")

    def do_DELETE(self):
        self.respond("DELETE")

def main():
    port = 8080
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()
