import socket
import struct

#Recived:  b'Username: vortex1 Password: Gq#qu3bF3'


client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_add=('vortex.labs.overthewire.org',5842)
client.connect(server_add)

total=0
for x in range(4):
    data=client.recv(4)
    total+=struct.unpack("<I",data)[0]
    

total=struct.pack("<I",(total & 0xFFFFFFFF))
client.send(total)

    
res=client.recv(1000)

print("Recived: ",res)
    
client.close()