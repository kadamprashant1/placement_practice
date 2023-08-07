
class Node:
    def __init__(self,data):
        self.__deta =data
        self.next=None


def insert(root, item):
    temp = Node(item)
    if root==None:
        return root
    else:
        ptr = temp
        while ptr.next != None:
            ptr =ptr.next
        ptr.next=temp
    return root

def convert(head):
    current = head
    
    while current.next != None:
        current = current.next
    current.next = head
    return head

def printdoubleLinked(head):
    start = head
    while(start.next != None and head.next != None):
        print(f'{head.data}',end="")
        head = head.next
        pass



def arrtolist(arr, n):
    root = None
    for i in range(0,n):
        root = insert(root, arr[i])
    return root



if __name__=='__main__':
    arr=[1,2,3,4,5]
    n = len(arr)
    root=arrtolist(arr, n)
    real=root
    root=convert(real)
    