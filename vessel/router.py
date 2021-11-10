from vessel.constants.requestMethods import ResponseMethods

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