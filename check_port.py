#!/usr/bin/python3
# Tested on Python 3.6.xx and 3.8.xx only (updated from Python 2.x)
import socket
 
# Create a new function 
def check_server_tcp_port(my_host_ip_name, my_tcp_port, timeout=5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((my_host_ip_name, my_tcp_port))
        print(f"TCP port {my_tcp_port} is open for the {my_host_ip_name}.")
        s.close()
        return True
    except socket.timeout:
        print(f"TCP port {my_tcp_port} is closed or timed out for the {my_host_ip_name}.")
        return False
 
# Test it 
check_server_tcp_port("localhost", 22 )
check_server_tcp_port("10.131.0.161", 22)
