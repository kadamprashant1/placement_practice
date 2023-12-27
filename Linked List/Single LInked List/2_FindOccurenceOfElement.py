class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

def insert(root, item):
    temp_ = Node(item)
    if root is None:
        root = temp_
    else:
        temp = root
        while temp.next is not None:
            temp = temp.next
        temp.next = temp_
    return root


def ArrToLinkedList(arr, n):
    root =None
    for i in range(n):
        root = insert(root,arr[i])
    return root

def occurence(root,element):
    temp1 = root
    count =0
    while temp1 :
        if temp1.data == element:
            count +=1
        temp1 = temp1.next
    return count

def display(root):
    temp_node=root
    while temp_node:
        print(temp_node.data, end="->")
        temp_node = temp_node.next
    print()

if __name__== "__main__":
    arr=[1,1,2,2,3]
    n = len(arr)
    root= ArrToLinkedList(arr, n)
    display(root)
    print("Occurence of element 1 in linked list")
    occur = occurence(root,1)
    display(root)
    print(f" occurence of 1 in linked list is {occur}")