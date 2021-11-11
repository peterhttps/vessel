import json
from vessel import vesselTCP
from vessel.request import VesselRequest
from vessel.router import VesselRouter 


class Vessel(vesselTCP.VesselTCP):
  def __init__(self):
    super().__init__()
    self.routes: list[VesselRequest] = []

  def attachRoutes(self, routesObject: VesselRouter):
    self.routes = routesObject.routes

  def printRoutes(self):
    print(self.routes)

  def handleRequest(self, data):

    request = VesselRequest(data)
    print(request.path, request.method)
    for route in self.routes:
      if (request.path == route.path and request.method == route.method):
        response = self.handle_GET(route)
        # response = handler(request)

        return response

    response = self.handle_GET(request)
    
    return response

  def handle_GET(self, request):
    if (request.function() != None):
      request.function()
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

