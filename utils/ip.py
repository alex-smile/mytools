import socket
import struct

# import netaddr


def ip2long(ipstr):
    return struct.unpack("!L", socket.inet_aton(ipstr))[0]


def long2ip(ipint):
    return socket.inet_ntoa(struct.pack("!L", ipint))


# def ip2long_v2(ipstr):
#     return int(netaddr.IPAddress(ipstr))


# def long2ip_v2(ipint):
#     return str(netaddr.IPAddress(ipint))


def get_local_ip():
    """Get server ip"""
    try:
        import fcntl
        import socket
        import struct

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack("256s", "eth1"))[20:24])  # SIOCGIFADDR
    except Exception:
        return "127.0.0.1"