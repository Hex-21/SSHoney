#!/usr/bin/env python3
import logging
import os.path
import paramiko
import socket
import threading

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", filename="logins.log", filemode="a")
logger = logging.getLogger("Logger")
logger.setLevel(logging.DEBUG)

lock = threading.Lock()


class honey(paramiko.ServerInterface):
    def check_auth_password(self, username: str, password: str):
        logger.info(f"USR:{username} PASSWORD:{password}")
        return paramiko.AUTH_FAILED

    def check_auth_publickey(self, username: str, key: paramiko.PKey):
        logger.info(f"USR:{username} PUBLICKEY:{key}")
        return paramiko.AUTH_FAILED


def connection(client, key):
    try:
        transport = paramiko.Transport(client)
        transport.add_server_key(key)
        transport.start_server(server=honey())
    except Exception as e:
        print(e)


def socket_server(ip="0.0.0.0", port=22):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((ip, port))
    sock.listen(10)

    key = paramiko.RSAKey.generate(2048)
    if os.path.isfile("private.pem"):
        key = paramiko.RSAKey(filename="private.pem")
    else:
        key.write_private_key_file(filename="private.pem")

    while True:
        client, addr = sock.accept()
        with lock:
            logger.info(f"Connection from {addr[0]}:{addr[1]}")
        conn_thread = threading.Thread(target=connection, args=(client, key), daemon=False)
        conn_thread.start()


if __name__ == "__main__":
    socket_server()
