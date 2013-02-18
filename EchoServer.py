#-*- encode: cp949 -*-


# < 서버 프로그램의 흐름 >
#
#       socket()      : 소켓을 생성한다.
#          |
#        bind()       : 소켓에 정보를 입력한다.
#          |
#       listen()      : 소켓을 연결 대기 상태로 만든다.
#          |
#       accept()      : 클라이언트의 연결 요청을 받아들인다.
#          |
#   send() & recv()   : 데이터를 주고받는다.


from socket import *


HOST = ''
PORT = 12328


# 소켓을 생성한다.
# 인터넷(AF_INET)을 사용하고, TCP프로토콜(SOCK_STREAM)을 사용한다.
server_sock = socket(AF_INET, SOCK_STREAM)

# 소켓에 정보(주소와 포트)를 입력한다.
server_sock.bind((HOST, PORT))

# 소켓을 연결 대기 상태로 만든다.
# 최대 5개까지 대기열에 넣는다.
server_sock.listen(5)

# 클라이언트의 연결 요청을 받아들인다.
conn, addr = server_sock.accept()

print('Connected by', addr)

# 데이터를 주고받는다.
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)

conn.close()
