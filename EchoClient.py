#-*- encode: cp949 -*-


# < 클라이언트 프로그램의 흐름 >
#
#       socket()      : 소켓을 생성한다.
#          |
#       connect()     : 서버에 연결한다.
#          |
#   send() & recv()   : 데이터를 주고받는다.

from socket import *

HOST = '127.0.0.1'
PORT = 12328

# 소켓을 생성한다.
# 인터넷(AF_INET)을 사용하고, TCP프로토콜(SOCK_STREAM)을 사용한다.
sock = socket(AF_INET, SOCK_STREAM)

# 서버에 연결한다.
# 입력한 주소(HOST)로 입력한 포트(PORT)를 통해 접속한다.
sock.connect((HOST, PORT))

# 데이터를 주고받는다.
sock.sendall(b'Hello World!')
data = sock.recv(1024)

print('Received', repr(data.decode()))

sock.close()
