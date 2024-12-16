import socket as so
d = input("Adj meg egy domaint! ")
s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.connect ((d, 80))
s.send (b"GET / HTTP1.1 \r\n Host: " + bytes (d, "UTF8") + b" \r\n connection: close \r\n\r\n")
reply = s.recv(10000)
s.shutdown(so.SHUT_RDWR)
s.close()
print (repr(reply))
