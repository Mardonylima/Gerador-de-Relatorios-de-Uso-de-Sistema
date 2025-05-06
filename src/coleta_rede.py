import re
import socket
import uuid


def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

def get_mac_address():
    mac = uuid.getnode()
    mac_str = ":".join(["{:02x}".format((mac >> ele) & 0xff) for ele in range(40, -1, -8)])
    return mac_str

