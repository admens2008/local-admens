from socket import *

def createServer():
	serverSocket = socket(AF_INET, SOCK_STREAM)
	try:
		serverSocket.bind(('localhost', 9000))
		serverSocket.listen(5)
		while(1):
			(clientSocket, address) = serverSocket.accept()	

			rd = clientSocket.recv(5000).decode()
			pieces = rd.split('\n')
			if (len(pieces) > 0):
				print(pieces[0])
			
			data = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Hello World</h1></body></html>"
			clientSocket.sendall(data.encode())
			clientSocket.shutdown(SHUT_WR)

	except KeyboardInterrupt:
		print("Shutting down server")
	except Exception as exc:
		print("Error: \n")
		print(exc)	

	serverSocket.close()

	print('Access http://localhost:9000')
createServer()