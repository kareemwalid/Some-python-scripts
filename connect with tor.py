import socks
import socket
from stem import Signal
from stem.control import Controller
from requests import get


def set_new_ip():
    """Change IP using TOR"""
    """with Controller.from_port(port=9050) as controller:
        controller.authenticate(password='PASSWORD')
        controller.signal(Signal.NEWNYM)
set_new_ip()
"""

ip = get('https://api.ipify.org').text
print(f'My IP address before Connecting with Tor is: {ip}')



socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
socket.socket = socks.socksocket

ip = get('https://api.ipify.org').text
print(f'My IP address after Connecting with Tor is: {ip}')
