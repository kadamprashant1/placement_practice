from collections import deque

class solution:
    def __init__(self) -> None:
        self.queue = deque()
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        else:
            raise IndexError(" queue is empty")
        
queue = solution()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue()) 