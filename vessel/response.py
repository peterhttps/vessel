

class VesselResponse:
  def __init__(self, statusCode=200):
    self.responseBody = {}
    self.statusCode = statusCode

  def json(self, jsonObj):
    self.responseBody = jsonObj

    return self

  def status(self, status):
    self.statusCode = status

    return self