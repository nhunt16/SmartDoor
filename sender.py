import socket
import time
import sys, os
import glob

def initialize(name):
	UDP_IP = "155.41.64.232"
	UDP_PORT = 5005
	buf = 1024

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	for filename in os.listdir("training_sets/" + name):
		if filename.endswith(".jpg"):
			f = open("training_sets/" + name + '/' + filename, "rb")
			data = f.read(buf)
			sock.sendto(filename.encode(), (UDP_IP, UDP_PORT))
			print(filename)
			while(data):
				if(sock.sendto(data, (UDP_IP, UDP_PORT))):
					data = f.read(buf)
					time.sleep(0.02)

	sock.close()
	f.close()