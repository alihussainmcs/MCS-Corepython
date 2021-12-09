"""
Python plays an essential role in network programming. The standard library of Python has full support for network
   protocols, encoding, and decoding of data and other networking concepts, and it is simpler to write network programs
    in Python than that of C++.

Here, we will learn about the essence of network programming concerning Python. But for this, the programmer must have
    basic knowledge of:


Low-Level Programming using sockets
Data encoding
HTTP and web-programming
High-Level client modules
Basic networking terms and their concepts etc.
Table of Contents
# Python Network Services
# Defining Socket
# Socket Program
# A Simple Network Program Using Python
There are two levels of network service access in Python. These are:

Low-Level Access
High-Level Access
In the first case, programmers can use and access the basic socket support for the operating system using Python's
    libraries, and programmers can implement both connection-less and connection-oriented protocols for programming.


Application-level network protocols can also be accessed using high-level access provided by Python libraries. These
    protocols are HTTP, FTP, etc.

A socket is the end-point in a flow of communication between two programs or communication channels operating over a
    network. They are created using a set of programming requests called socket API (Application Programming Interface).
    Python's socket library offers classes for handling common transports as a generic interface.

Sockets use protocols for determining the connection type for port-to-port communication between client and server
    machines. The protocols are used for:


Domain Name Servers (DNS)
IP addressing
E-mail
FTP (File Transfer Protocol) etc...
Python has a socket method that let programmers' set-up different types of socket virtually. The syntax for the socket
    method is:
              g = socket.socket (socket_family, type_of_socket, protocol=value)
For example_1, if we want to establish a TCP socket, we can write the following code snippet:
"""

import socket
# Take server name
host = 'www.google.com'

try:
    # To know IP Address of any website
    addr = socket.gethostbyname(host)
    print("IP Address of website ", addr)
    print("Host Address of website ", socket.gethostbyaddr(host))
    print("Host HostName ex of website ", socket.gethostbyname_ex(host))
    print("Host Name of website ", socket.gethostname())
except socket.gaierror:
    print("Website doesn't exist")


print("--------------------------------------------------------------------")
# Take server name
host = 'www.paytm.com'

try:
    # To know IP Address of any website
    addr = socket.gethostbyname(host)
    print("IP Address of website ", addr)
    print("Host Address of website ", socket.gethostbyaddr(host))
    print("Host HostName ex of website ", socket.gethostbyname_ex(host))
    print("Host Name of website ", socket.gethostname())
except socket.gaierror:
    print("Website doesn't exist")

print("-------------------------------------------------------------------------------")
# Take server name
host = 'www.alian.com'

try:
    # To know IP Address of any website
    addr = socket.gethostbyname(host)
    print("IP Address of website ", addr)
    print("Host Address of website ", socket.gethostbyaddr(host))
    print("Host HostName ex of website ", socket.gethostbyname_ex(host))
    print("Host Name of website ", socket.gethostname())
except socket.herror as se:
    print("Website doesn't exist", se)

'''
Socket API Overview
Python’s socket module provides an interface to the Berkeley sockets API. This is the module that we’ll use and discuss 
in this tutorial.

The primary socket API functions and methods in this module are:

socket()
bind()
listen()
accept()
connect()
connect_ex()
send()
recv()
close()
'''