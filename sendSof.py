import os
import requests
import sys 
# Port on which server will run.



def send_file(name):
    endpoint = "http://10.42.0.158:9000/received/"
    endpoint += name

    payload1 = open(name, 'rb').read()
    request1 = requests.post(endpoint, data=payload1, headers={'Content-Type': 'application/xml'})
    print (request1.text)
    return

 
# Get the total number of args passed to the demo.py
total = len(sys.argv)
 
if total==2:
    send_file(str(sys.argv[1])) 
else:
    print("Usage: python sendFile.py <filename>")
