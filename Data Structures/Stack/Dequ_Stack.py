# How to use deque as Stack as well

from collections import deque

stack = deque()
stack.append(12)
stack.append(90)
stack.append(89)

print(stack)

print(stack[-1])
print(stack.pop())