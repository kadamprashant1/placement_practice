class solution:
    def __init__(self) -> None:
        self.queue=[]
    def enqueue (self, item):
        self.queue.append(item)
    def dequeue (self):
        if self.queue:
            return self.queue.pop(0)
        else:
            raise IndexError("queue is empty")

queue = solution()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue()) 