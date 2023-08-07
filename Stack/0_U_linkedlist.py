# Why to use linked list in stack
#-> size of stack is not known in advance
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = Node
    
class Stack:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, data):
        if self.head ==None:
            self.head=Node(data)
        else:
            newnode =Node(data)
            newnode.next=self.head
            self.head = newnode
    
    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False

    

    def display(self):
        itnode=self.head
        if self.isEmpty():
            print("stack is underflow")
        else:
            while itnode !=None:
                print(itnode.data, end=" ")
                itnode=itnode.next

    
if __name__=="__main__":
    mystack= Stack()
    mystack.push(1)
    mystack.push(2)
    mystack.push(3)
    mystack.push(4)

    #display element
    mystack.display()
