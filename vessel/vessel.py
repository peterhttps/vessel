import json
from vessel import vesselTCP
from vessel.request import VesselRequest
from vessel.response import VesselResponse
from vessel.router import VesselRouter 


class Vessel(vesselTCP.VesselTCP):
  def __init__(self):
    super().__init__()
    self.routes: list[VesselRequest] = []

  def attachRoutes(self, routesObject: VesselRouter):
    self.routes = routesObject.routes

  def handleRequest(self, data):

    request = VesselRequest(data)

    for route in self.routes:
      if (request.path == route.path and request.method == route.method):
        route.headers = request.headers
        response = self.handle_GET(route)
        # response = handler(request)

        return response

    response = VesselResponse(statusCode=501)
    
    return self.handle_GET(response)

  def handle_GET(self, request: VesselRequest):
    
    response = VesselResponse()

    if (request.function != None):
      request.function(request, response)
    responseLine = "HTTP/1.1 %s OK\r\n" % (response.statusCode)
    responseLine = responseLine.encode()
    headers = self.response_headers()

    blankLine = b"\r\n"

    testResponse = response.responseBody

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

