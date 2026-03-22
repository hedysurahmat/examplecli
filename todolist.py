todos=[]
while True:
    cmd=input("> ")
    if cmd=="add": todos.append(input("task: "))
    elif cmd=="list": print(todos)
    elif cmd=="del": todos.pop(int(input("index: ")))
