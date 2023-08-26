class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next=None
        self.prev=None

class Stack:
    def __init__(self) -> None:
        self.head=None
    
    def push(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev = new_node
            self.head =new_node

    def pop(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head.val
            self.head = self.head.next
            self.head.prev = None
            return temp

    def top(self):
        if self.head is None:
            return None
        else:
            return self.head.val
        
    def size(self):
        count=0
        current = self.head
        while current is not None:
            count +=1
            current = current.next
        return count
    
    def printstack(self):
        current = self.head
        while current is not None:
            print(current.val , end=" ")
            current= current.next
s =Stack()
s.push(4)
s.push(6)
s.push(2)
s.push(1)
s.push(8)
s.printstack()
print("\nTop element is", s.top())
print(f"size {s.size()}")




