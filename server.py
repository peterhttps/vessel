import os, sys
sys.path.insert(0, os.path.abspath(".."))
from vessel.vessel import Vessel
from routes import router

if __name__ == '__main__':
  server = Vessel()

  server.attachRoutes(router)

  server.start()

