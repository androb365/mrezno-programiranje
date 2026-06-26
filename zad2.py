import socket

def print_remote_machine_info():
    domain = "google.com"
    ip_address = socket.gethostbyname(domain)
    print("IP adresa od %s je: %s" % (domain, ip_address))

if __name__ == '__main__':
    print_remote_machine_info()
