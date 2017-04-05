import zmq
import socket

data = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def writefile(sor):
    with open("log0.txt",'a') as f:
        f.write(sor)
        f.close()
        
def tcp_stream():
    global sock, data
    dataTemp = ""
    while '\n' not in dataTemp:
        dataTemp += str(sock.recv(2048),"utf-8")
    dataTemp = dataTemp.strip("\r\n").split(";")
    #print(dataTemp)
    data.append(dataTemp)
    #writefile(dataTemp)
    return dataTemp[3]

def test(): # ZeroMq kapcsolat tesztelése
    return "It works!"

def zeromq():
    global context, socket
    #  Wait for request from client
    message = socket.recv()
    print("Received request: %s" % message)

    try:
        r = eval(message)
        print(r)
        socket.send(bytearray(str(r), 'utf-8'))  # send returned value as bytearry to client
    except NameError:
        socket.send(b"Unknown command")
    except:
        socket.send(b"Unknown error")

def tcp_conn(IPcim):
    global sock
    # TCP Setup 
    sock.connect((IPcim,234))

# ZeroMq configuráció
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5555") 

tcp_conn("192.168.137.227")
while True:
    zeromq()

