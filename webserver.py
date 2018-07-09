from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#import SimpleHTTPServer
import time
import SocketServer

class serverHandler (BaseHTTPRequestHandler):
  def do_GET(self):
    try:
      if self.path.endswith(".html"):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
      #message
        self.wfile.write("Hello, Welcome to epic server")
        return
    except IOError:
        self.send_error(404, 'File Not Found: %s' % self.path)

def main():
  try:
    port = 9000
    server = HTTPServer(('',port), serverHandler)
    print "Server running on port %s" % port
    server.serve_forever()
  except KeyboardInterrupt:
    print "^C entered, server shutting down..."
    server.scoket.close()

if __name__ == '__main__':
  main()