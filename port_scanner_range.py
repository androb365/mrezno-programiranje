import socket

socket.setdefaulttimeout(0.5)

host = input("Unesite host (IP ili domena): ")
start_port = int(input("Unesite početni port (1-65535): "))
end_port = int(input("Unesite krajnji port (1-65535): "))

if start_port < 1 or end_port > 65535 or start_port > end_port:
    print("Neispravan raspon portova!")
else:
    print(f"\nOtvoreni portovi na {host}:")
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex((host, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "nepoznat"
                print(f"- {port} ({service})")
