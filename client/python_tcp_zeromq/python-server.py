import zmq
import socket

data = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def tcp_stream():
    global sock, data
    dataTemp = ""
    while '\n' not in dataTemp:
        dataTemp += str(sock.recv(2048),"utf-8")
    dataTemp = dataTemp.strip("\r\n").split(";")
    #print(dataTemp)
    data.append(dataTemp)
    #writefile(dataTemp)
    return dataTemp

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
    except Exception as error:
        print(error)
        socket.send(b"Unknown error")

def tcp_conn(IPcim):
    global sock
    # TCP Setup 
    sock.connect((IPcim,234))

def main():
    return ";".join(tcp_stream())

# ZeroMq configuráció
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5555") 

tcp_conn("192.168.137.119")

while True:
    zeromq()