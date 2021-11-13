from vessel.request import VesselRequest
from vessel.response import VesselResponse
from vessel.router import VesselRouter

router = VesselRouter()

def testPrint(req: VesselRequest, res: VesselResponse):
  resp = {
    "id": 1999,
    "name": "John",
    "age": 28
  }

  res.status(200).json(resp)

def testPost(req: VesselRequest, res: VesselResponse):
  resp = {
    "id": 2222,
    "name": "Mary",
    "age": 35
  }

  res.status(200).json(resp)


router.get('/casa', testPrint)
router.post('/postReq', testPost)

