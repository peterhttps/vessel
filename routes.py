from vessel.request import VesselRequest
from vessel.response import VesselResponse
from vessel.router import VesselRouter

router = VesselRouter()

def testPrint(request: VesselRequest, response: VesselResponse):
  resp = {
    "id": 1999,
    "name": "John",
    "age": 28
  }

  print(request.headers)

  response.status(200).json(resp)

router.get('/casa', testPrint)

