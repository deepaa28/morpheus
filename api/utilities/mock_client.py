import socket
import ssl
from urllib.request import urlopen

host = socket.gethostname()
port = 8000
sock = socket.socket()
sock.connect((host, port))

# start the video stream
CONTEXT = ssl._create_unverified_context()
URL = "https://192.168.43.1:8080/shot.jpg"

while True:
    s = urlopen(URL, context=CONTEXT)
    imgResp = s.read()
    imgResp = str(imgResp)
    mess = sock.recv(1024).decode('utf-8')
    sock.send(imgResp.encode('utf-8'))
    data = sock.recv(1024).decode('utf-8')
    print(data)

sock.close()
