

class VesselResponse:
  def __init__(self):
    self.responseBody = {}
    self.statusCode = 200

  def json(self, jsonObj):
    self.responseBody = jsonObj

  def status(self, status):
    self.statusCode = status