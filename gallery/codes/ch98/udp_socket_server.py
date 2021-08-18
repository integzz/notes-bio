import SocketServer


# The RequestHandler class for our server.
class TCPRequestHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]} wrote:")
        print(self.data)
        # Sending the same data
        self.request.sendall(self.data)
        # Create the server, binding to localhost on port 8090
        server = SocketServer.TCPServer(("", 8090), TCPRequestHandler)
        # Activate the server; this will keep running untile we interrupt
        server.serve_forever()
