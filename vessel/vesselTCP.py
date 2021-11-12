import socket 

class VesselTCP:
  headers = {
        'Content-Type': 'application/json',
  }

  status_codes = {
        200: 'OK',
        404: 'Not Found',
  }

  def __init__(self, host='127.0.0.1', port=8888):
    self.host = host
    self.port = port

  def start(self):
    socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socketObject.bind((self.host, self.port))

    socketObject.listen(5)

    print("Server is Running at", socketObject.getsockname())

    while True:
      conn, addr = socketObject.accept()

      print("Connected by", addr)

      data = conn.recv(1024)

      response = self.handleRequest(data)
      
      conn.sendall(response)

      conn.close()

  def handleRequest(self, data):
    return data
