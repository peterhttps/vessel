from main import Vessel, VesselRouter


if __name__ == '__main__':
  server = Vessel()
  router = VesselRouter()

  router.get('/casa')
  # router.get('/teste')

  server.attachRoutes(router)

  # server.printRoutes()
  server.start()

