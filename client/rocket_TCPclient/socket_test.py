import socket

with open("log2.txt",'w') as f:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("192.168.0.31",234))
    while True:
        dataTemp = ""
        while '\n' not in dataTemp:
            dataTemp += str(sock.recv(2048),"utf-8")
        f.write(dataTemp)
        print(dataTemp.strip("\r\n").split(";"))
        
