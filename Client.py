import socket
import os

try:
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
except Exception as err:
	print("Failed cuz...", str(err))

try:
	os.system("clear")
	host = socket.gethostname()

	def pnum():
		while True:
			try:
				pn = input("Type port you want to connect on: ")
				port = int(pn)
				return port
			except ValueError:
				print("Invalid port number, try again...")
	port = pnum()

	soc.connect((host, port))
	print("Connected successfully to [host =", host, "] [port =", port, "]")
	try:
		msg = soc.recv(1024)
		print("Message from server is: ", msg.decode())
		
	except Exception as e:
		print("Failed to receive message from server...", str(e))
	soc.close()
except Exception as e:
	print("Failed cuzof...", str(e))
	
			