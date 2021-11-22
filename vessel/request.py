from vessel.constants.requestMethods import ResponseMethods
from ast import literal_eval
from http_parser.pyparser import HttpParser

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
    p = HttpParser()
    nparsed = p.execute(data, len(data))

    assert nparsed == len(data)

    if p.is_headers_complete():
      print(p.get_headers())
      for key, value in p.get_headers().items():
        self.headers[key] = value

    lines = data.split(b"\r\n")

    requestLine = lines[0]
    words = requestLine.split(b" ")

    if (words[0].decode() == "GET"):
      self.method = ResponseMethods.GET
    elif (words[0].decode() == "POST"):
      self.method = ResponseMethods.POST
    elif (words[0].decode() == "PUT"):
      self.method = ResponseMethods.PUT

    if len(words) > 1:
      self.path = words[1].decode()

    if len(words) > 2:
      self.http_version = words[2]
               
    if (words[0].decode() != "GET"):
      pieces = data.decode().split('\r\n\r\n')

      body = '\r\n\r\n'.join(pieces[1:])
        
      self.body = literal_eval(body)
