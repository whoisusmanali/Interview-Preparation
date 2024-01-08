from collections import deque

Names = deque()
Names.append("Usman")
Names.append("ali")
Names.append("Sattar")

while len(Names) > 0:
    name = Names.popleft()
    print(name)


