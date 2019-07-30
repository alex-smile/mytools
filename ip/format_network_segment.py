#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: alex-smile
# @date: 20190726

import sys
import socket
import struct


def ip2long(ipstr):
    return struct.unpack("!L", socket.inet_aton(ipstr))[0]


def long2ip(ipint):
    return socket.inet_ntoa(struct.pack("!L", ipint))


def format_network_segment(ips):
    for ip in ips:
        ip_net_mask = ip.split("/")
        if len(ip_net_mask) == 1:
            ip_net, mask = ip, 32
        elif len(ip_net_mask) == 2:
            ip_net, mask = ip_net_mask
        else:
            print "{} is not valid ip".format(ip)
            continue
        mask = int(mask)
        ip_net = long2ip(ip2long(ip_net) >> (32 - mask) << (32 - mask))
        print "{:16} => {}/{}".format(ip, ip_net, mask)


if __name__ == "__main__":
    ips = sys.argv[1:]
    format_network_segment(ips)
