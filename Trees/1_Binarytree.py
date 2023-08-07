
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left =Node(data)
                else:
                    self.left.insert(data)
            elif data >self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else: 
            self.right.insert(data)

    def preorder(self):
        if self.left:
            self.left.preorder()
        print(self.data)
        if self.right:
            self.right.preorder()

if __name__=="__main__":
    root = Node(1)
    root.insert(2)
    root.insert(3)
    root.insert(6)
    root.insert(5)
    root.insert(4)
    root.preorder()
    

