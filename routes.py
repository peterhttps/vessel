from vessel.router import VesselRouter

router = VesselRouter()

def testPrint():
  print("HIII REQUEST")

router.get('/casa', testPrint)

