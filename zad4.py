import socket

def network_activity():
    hostname, aliases, ip_list = socket.gethostbyaddr("8.8.8.8")
    print("Hostname: %s" % hostname)
    print("IP lista: %s" % ip_list)

if __name__ == '__main__':
    network_activity()
