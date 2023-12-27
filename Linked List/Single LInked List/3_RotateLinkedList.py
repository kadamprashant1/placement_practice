class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

def insert(root,item):
    temp = Node(item)
    if root ==None:
        root = temp
    else:
        ptr = root
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = temp
    return root

def ArrToList(arr, n)->Node:
    root = None
    for i in range(n):
        root = insert(root, arr[i])
    return root

def display(root):
    temp_node=root
    while temp_node:
        print(temp_node.data, end="->")
        temp_node = temp_node.next
    print()

def rotateRight(root,n):
    temp = root
    if root == None or n == 0:
        return temp
    length = 1
    curr = temp
    while curr.next:
        length +=1
        curr = curr.next
    n = n % length
    for _ in range(length - n - 1):
        temp = temp.next
    new_node = temp.next
    temp.next = None # disconnect 
    temp = new_node
    while temp.next :
        temp=temp.next
    temp.next = root
    return new_node



if __name__ == "__main__":
    arr=[1,2,3,4,5]
    n = len(arr)
    root= ArrToList(arr, n)
    display(root)
    print("After rooteting array by 2 :")
    root=rotateRight(root,2)
    display(root)