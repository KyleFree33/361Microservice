# Microservice:

# Requesting Data
If data is received it is decoded and read. Then it is adjusted to the new weight and reps via the microservice and sent back.
```python
while True:
    rec = sock.recv(1024).decode("utf-8")
    if rec == '':
        # sc, addr = s.accept()
        break
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
