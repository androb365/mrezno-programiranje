import socket
import datetime
from local_machine_info import print_machine_info

print_machine_info()
print(datetime.datetime.now())

HOST = '0.0.0.0'
PORT = 65434

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[ECHO SERVER] Listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"[ECHO SERVER] Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                poruka = data.decode()
                print(f"[ECHO SERVER] Received: {poruka} from {addr}")
                if poruka == "vaše_ime_prezime":
                    conn.sendall("Unos nije podržan.".encode())
                else:
                    conn.sendall(data)
