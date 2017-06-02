import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.106.130', 6900)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
# The AES key used for encrytp/decrypt is "3DF2104AB016B2DE" 
# below room is 3
message = ('{ "command": "main", "x": ' 
		'"B8E65C3EB25022E2EFB6E4953BE25CBB",'
		' "y": "76834D38CD1B828B83A229D03198B38C",'
		' "room":"5C3350B0DB38B5EC1820C2EAADAD2D74' 	
		'"}')
print >>sys.stderr, 'sending "%s"' % message
sock.sendall(message)

# Look for the response
amount_received = 0
amount_expected = 400
    
while amount_received < amount_expected:
   data = sock.recv(16)
   amount_received += len(data)
   print >>sys.stderr, 'received "%s"' % data


print >>sys.stderr, 'closing socket'
sock.close()












