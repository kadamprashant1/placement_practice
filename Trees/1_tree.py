class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None 
        self.right=None

    def preorder(self):
       if self.left:
           self.left.preorder()
       print(self.data,end=" ")
       if self.right:
           self.right.preorder()
       
    def postorder(self):
        if self.right:
            self.right.postorder()
        print(self.data,end=" ")
        if self.left:
            self.left.postorder()

    def inorder(self):
        if self.data is None:
            return
        else :
            print(self.data,end=" ")
            if self.left:
                self.left.inorder()
            self.right.inorder()
            


if __name__=="__main__":
    root = Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right= Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    print("pre-order")
    root.preorder()
    print("\nin-order")
    root.inorder()
    print("\npost-order")
    root.postorder()
