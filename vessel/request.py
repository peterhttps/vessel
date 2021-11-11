from vessel.constants.requestMethods import ResponseMethods


class VesselRequest:
  def __init__(self, data=None, method=None, path=None, function=None):
    self.method = method
    self.path = path
    self.httpVersion = "1.1"
    self.function = function

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