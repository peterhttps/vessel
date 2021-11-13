from vessel.constants.requestMethods import ResponseMethods
from ast import literal_eval

class VesselRequest:
  def __init__(self, data=None, method=None, path=None, function=None, isImplemented=True):
    self.method = method
    self.path = path
    self.httpVersion = "1.1"
    self.function = function
    self.headers = {}
    self.body = {}
    self.isImplemented = isImplemented

    if (data != None):
      self.parse(data)

  def parse(self, data):
    lines = data.split(b"\r\n")

    requestLine = lines[0]
    words = requestLine.split(b" ")

    if (words[0].decode() == "GET"):
      self.method = ResponseMethods.GET

    if len(words) > 1:
      self.path = words[1].decode()

    if len(words) > 2:
      self.http_version = words[2]

    if (len(lines) > 1):
      headersTemp = lines[1:]
      for headerString in headersTemp:
        headerKeyValue = headerString.decode().split(":", 1)

        if (headerKeyValue[0] != ''):
          self.headers[headerKeyValue[0]] = headerKeyValue[1]

      pieces = data.decode().split('\r\n\r\n')

      body = '\r\n\r\n'.join(pieces[1:])
      
      self.body = literal_eval(body)
