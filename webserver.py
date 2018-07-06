from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#import SimpleHTTPServer
import time
import SocketServer

class serverHandler (BaseHTTPRequestHandler):
  def do_GET(self):
    try:

    except:

def main()
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