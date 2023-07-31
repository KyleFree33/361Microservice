# Microservice:

# Requesting Data
If data is received it is decoded and read. Then it is adjusted to the new weight and reps via the microservice and sent back.
```python
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
```

# Receiving Data
- While the program is sleeping after sending the log list, the microservice responds by writing the number of values back to count.txt
- Then the rest of the code is executed: 
```python
with open('count.txt', 'r') as infile:
    count = infile.readline()
    print(count + " Total days logged")
```
- The count is read from the file and displayed to the user

# UML Sequence Diagram
[UML Diagram.pdf](https://github.com/KyleFree33/361Microservice/files/12221917/UML.Diagram.pdf)
