import os
import socket

try:
	#Creating a socket for connections:
	soc = socket.socket(socket.AF_INET, 		socket.SOCK_STREAM)
	
except Exception as eer:
	print("There was an error initiailizing socket...", str(eer))

try:
	#Now we declare a port and server address:
		
	os.system("clear")
	pn = input("Type port you want to host on: ")
	host = socket.gethostname()
	port = pn
	
	try:
		port = int(pn)
		print("Server hosted on port...(", pn, ")")
	except:
		print("Invalid port number, default port would be used")
		port = 8888
	
	#Lets bind the host and port to our socket:
	soc.bind((host, port))
	
except Exception as err:
	print("Binding finalized", str(err))

try:
	#Now, let's listen for connections:
		soc.listen(5)
		
		print("Now listening for connection.........")
		while True:
			try:
				cli, s_addr = soc.accept()
				#Let's print whether connection successful or not:
				print("Received connection from ", str(s_addr))
				
				msg = input("Type message u want to send..: ")
				try: 
					cli.send(msg.encode())
					print("Message sent successfully")
				
				except Exception as ii:
					print("Could not send message to client...Error ", str(ii))
				
				print("\nListening for new connection(s).......\n")
				
				cli.close()
			
			except Exception as er:
				print("Error msg is....", str(er))
				
except Exception as eerr:
	print("Error message is...", str(eerr))
	
	
