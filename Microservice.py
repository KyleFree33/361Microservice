import socket

active_socket = socket.socket()
active_socket.bind(("0.0.0.0", 60))
active_socket.listen(1)  # clients permitted connect
print("server activated...")

sock, addr = active_socket.accept()

while True:
    rec = sock.recv(1024).decode("utf-8")
    if rec == '':
        # sc, addr = s.accept()
        break
    else:
        print(f"Received {rec!r}")
        rec = rec.split(" ")
        new_weight = int(rec[0]) * 1.05
        new_reps = int(rec[1]) - 2
        response = (str(new_weight) + " " + str(new_reps)).encode("utf-8")

        sock.send(response)

print("closing server...")

sock.close()
active_socket.close()
