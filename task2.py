
from ipaddress import IPv4Address


def int32_to_ip(int32):
    return IPv4Address(int32)


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"

int32 = int(input())
print(int32_to_ip(int32))
