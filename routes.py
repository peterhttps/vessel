from vessel.response import VesselResponse
from vessel.router import VesselRouter

router = VesselRouter()

def testPrint(response: VesselResponse):
  resp = {
    "id": 1999,
    "name": "John",
    "age": 28
  }

  response.status(200).json(resp)

router.get('/casa', testPrint)

