from vessel.router import VesselRouter
from vessel.vessel import Vessel


if __name__ == '__main__':
  server = Vessel()
  router = VesselRouter()

  router.get('/casa')

  server.attachRoutes(router)

  server.start()

