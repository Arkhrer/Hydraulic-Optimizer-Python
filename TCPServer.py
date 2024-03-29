import socket
import Globals

def TCPserver(host, port):

    while True:
        try:
            tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tcp_server.bind((host, port))
            break
        except socket.error:
            # print("Falha na conexão. Reconectando")
            pass

    tcp_server.listen()
    conn, addr = tcp_server.accept()
    result = ""

    while 1:
        data = conn.recv(1024)
        if not data:
            break

        result = data.decode("utf-8")
        # print("Recieved result ", result)
        
        conn.sendall(data)

    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

    Globals.threadState[port] = 1

    return result

if __name__ == '__main__':
    TCPserver("localhost", 9001)