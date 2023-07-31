# Microservice:

# Requesting Data
If data is received it is decoded and read. Then it is adjusted to the new weight and reps via the microservice and sent back.
```python
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"135, 10")
    data = s.recv(1024)

print(f"Received {data!r}")
```
Example Call: 

# Receiving Data
The microservice receives the response, adjusts the values, and sends back a response.
```python
print(f"Received {rec!r}")
        rec = rec.split(" ")
        new_weight = int(rec[0]) * 1.05
        new_reps = int(rec[1]) - 2
        response = (str(new_weight) + " " + str(new_reps)).encode("utf-8")
        sock.send(response)
```
Example Call: 

# UML Sequence Diagram
[UML Diagram.pdf](https://github.com/KyleFree33/361Microservice/files/12221935/UML.Diagram.pdf)
