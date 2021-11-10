from enum import Enum
import socket 
import json 

class ResponseMethods(Enum):
  GET = 1

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

    if (words[0].decode() == "GET"):
      self.method = ResponseMethods.GET

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

class VesselRouter:
  def __init__(self):
    self.routes = []

  def get(self, path, function=None):
    routeType = {
      "method": ResponseMethods.GET,
      "path": path,
      "function": function
    }

    self.routes.append(routeType)

class Vessel(VesselTCP):
  def __init__(self):
    super().__init__()
    self.routes = []

  def attachRoutes(self, routesObject: VesselRouter):
    self.routes = routesObject.routes

  def printRoutes(self):
    print(self.routes)

  def handleRequest(self, data):

    request = VesselRequest(data)
    print(request.uri, request.method)
    for route in self.routes:
      if (request.uri == route["path"] and request.method == route["method"]):
        response = self.handle_GET(request)
        # response = handler(request)

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
      reason = self.status_codes[status_code]
      line = "HTTP/1.1 %s %s\r\n" % (status_code, reason)

      return line.encode() 

  def response_headers(self, extra_headers=None):
      headers_copy = self.headers.copy() 
      if extra_headers:
          headers_copy.update(extra_headers)

      headers = ""

      for h in headers_copy:
          headers += "%s: %s\r\n" % (h, headers_copy[h])

      return headers.encode() 



# if __name__ == '__main__':
#   server = Vessel()
#   server.start()