import socket
 
sock = socket.socket()
adr=''
port=4188
sock.bind((adr, port))
if adr=='':
    print('Starting server open on all interfaces')
else:
    print(f'Starting server open on {adr}')

print(f'Start listening {port}')
while True:
    sock.listen(1)
    
    conn, addr = sock.accept()
    print('connected:', addr)

    while True:
        data = conn.recv(1024).decode()
        if data:
            print(f'Message recieved from {addr}')
        if not data:
            print('Client disconnected')
            break
        conn.send(data.upper().encode())
        print(f'Message echoed to {addr}')
    break
conn.close()
print('Closing connection, stopping server')
