from vessel.constants.requestMethods import ResponseMethods


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