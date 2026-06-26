import socket

socket.setdefaulttimeout(0.5)

host = input("Unesite host (IP ili domena): ")
port = int(input("Unesite port: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    result = s.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} je OTVOREN na {host}")
    else:
        print(f"Port {port} je ZATVOREN na {host}")
