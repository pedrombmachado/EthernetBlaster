
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 18:45:32 2016

@author: pedromachado
"""

from http.server import BaseHTTPRequestHandler,HTTPServer
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
from subprocess import Popen, PIPE
import sys
import shlex
import time
PORT = 9000
serverIP='10.42.0.158'

class HTTPRequestHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		""" Handle POST Request"""
		# Check if path is there.
		if self.path:
			# Get length of the data and read it.
			length = self.headers['content-length']
			if int(length)==31731266:
				if self.path[len(self.path)-3:len(self.path)]=="sof":
					data = self.rfile.read(int(length))
					# Write the data to a file in current dir.
					with open("/home/pedro/Ethernet_Blaster/" + self.path, 'wb+') as file:
						file.write(data)
					string="File " + self.path[10:len(self.path)] + " was accepted! at "+time.strftime("%d/%m/%Y %H:%M:%S")+"\n"
					print(string)
					self.send_response(200)
					self.send_header("Content-type", "text/html")
					self.end_headers()
					log="The file was received with success!\nThe process to program the FPGA has started and it will take about 1 minute to complete!\n"
					print(log)
					path="P;"+"/home/pedro/Ethernet_Blaster"+ self.path
					path+="@1"
					par1="/home/pedro/altera/16.0/qprogrammer/bin/quartus_pgm"
					par2="-z"
					par3="--mode=JTAG"
					par4="-o"
					par5=path
					cmd=par1+" "+par2+" "+par3+" "+par4+" "+par5
					process = Popen(shlex.split(cmd), stdout=PIPE)
					(output, err)=process.communicate()
					self.wfile.write(output)
					exit_code = process.wait()
					log="Deleting file "+self.path[10:len(self.path)]+"!\n"
					print(log)
					os.remove("/home/pedro/Ethernet_Blaster/" + self.path)
					log="File deleted.\n"
					print(log)
					if exit_code==0:
						log="The FPGA was configured with success!\n"
					else:
						log="ERROR! The FPGA was NOT configured!\n"
					exit_code="Exit code: "+str(exit_code)+"\n"
					err="External code error: "+str(err)+"\n"
					self.wfile.write(log.encode())
					self.wfile.write(err.encode())
					self.wfile.write(exit_code.encode())
					print(exit_code)
					print(err)
					print(log)
				else:
					log="ERROR: File size error!\nThe FPGA was NOT configured!\nExit code: -1\n"
					self.wfile.write(log.encode())
					print(log)
			else:
				log="ERROR: Empty packet!\nThe FPGA was NOT configured!\nExit code: -2\n"
				self.wfile.write(log.encode())
				print(log)

if __name__ == "__main__":
    # Create the server
    server = HTTPServer((serverIP, PORT), HTTPRequestHandler) 
    print("Files server serving endpoint: ", serverIP, ":", PORT)
    print("Server online since:", time.strftime("%d/%m/%Y %H:%M:%S"))

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()
