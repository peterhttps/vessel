import socket 
import json 

class VesselRequest:
  def __init__(self, data):
    self.method = None
    self.uri = None
    self.httpVersion = "1.1"

    self.parse(data)

  def parse(self, data):
    lines = data.split(b"\r\n")

    requestLine = lines[0]
    words = requestLine.split(b" ")

    self.method = words[0].decode()

    if len(words) > 1:
      self.uri = words[1].decode()

    if len(words) > 2:
      self.http_version = words[2]

class VesselTCP:
  headers = {
        'Server': 'VesselServer',
        'Content-Type': 'application/json',
  }

  status_codes = {
        200: 'OK',
        404: 'Not Found',
  }

  def __init__(self, host='127.0.0.1', port=8888):
    self.host = host
    self.port = port

  def start(self):
    socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socketObject.bind((self.host, self.port))

    socketObject.listen(5)

    print("Server is Running at", socketObject.getsockname())

    while True:
      conn, addr = socketObject.accept()

      print("Connected by", addr)

      data = conn.recv(1024)

      response = self.handleRequest(data)
      
      conn.sendall(response)

      conn.close()

  def handleRequest(self, data):
    return data

class Vessel(VesselTCP):
  def handleRequest(self, data):

    request = VesselRequest(data)
    handler = getattr(self, 'handle_%s' % request.method)

    response = handler(request)

    return response

  def handle_GET(self, request):

    responseLine = b"HTTP/1.1 200 OK\r\n"
    headers = self.response_headers()

    blankLine = b"\r\n"

    testResponse = {
      "id": 20,
      "name": "John",
      "country": "UK"
    }

    responseBody = json.dumps(testResponse, indent=2).encode(encoding = 'UTF-8')

    return b"".join([responseLine, headers, blankLine, responseBody])

  def response_line(self, status_code):
      """Returns response line"""
      reason = self.status_codes[status_code]
      line = "HTTP/1.1 %s %s\r\n" % (status_code, reason)

      return line.encode() # call encode to convert str to bytes

  def response_headers(self, extra_headers=None):
      headers_copy = self.headers.copy() # make a local copy of headers

      if extra_headers:
          headers_copy.update(extra_headers)

      headers = ""

      for h in headers_copy:
          headers += "%s: %s\r\n" % (h, headers_copy[h])

      return headers.encode() # call encode to convert str to bytes

class VesselRouter(VesselTCP):


if __name__ == '__main__':
  server = Vessel()
  server.start()