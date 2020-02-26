#!/usr/bin/env python

from urllib.parse import urlparse
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
import classify_nsfw
import weapon_classify


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        

    def do_GET(self):
        self._set_headers()
        print (self.path[1:])
        try:
            message = classify_nsfw.get_score(self.path[1:])  
            message_new = weapon_classify.get_scores(self.path[1:]) 

        except Exception as e:
            logging.exception("ok")
            message = "exception: " + e.message
            message_new = "exception: " + e.message_new
        #self.wfile.write(b'\n')
        self.wfile.write(str(message).encode("utf-8"))
       
        self.wfile.write(b'\n,\n')
        self.wfile.write(str(message_new).encode("utf-8"))



    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("".encode("utf-8"))


def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
