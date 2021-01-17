# Following mosh's lecture 5.14:

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft()

print(queue)

#outputs: deque([2, 3])
