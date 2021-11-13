from vessel.constants.requestMethods import ResponseMethods
from vessel.request import VesselRequest

class VesselRouter:
  def __init__(self):
    self.routes = []

  def get(self, path, function=None):
    request = VesselRequest(method=ResponseMethods.GET, path=path, function=function)

    self.routes.append(request)

  def post(self, path, function=None):
    request = VesselRequest(method=ResponseMethods.POST, path=path, function=function)

    self.routes.append(request)