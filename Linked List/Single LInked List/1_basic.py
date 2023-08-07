import math

class Node:
    def __init__(self,data):
        self.data =data
        self.next =None

def sizelinked(root):
    if(root==None):
        return 0
    else:
        return 1+sizelinked(root.next)

def insert(root,item):
    temp = Node(item)
    if root==None:
        root=temp
    else:
        ptr=root
        while ptr.next!=None:
            ptr=ptr.next
        ptr.next=temp
    
    return root

def reverse(root):
    if root is None or root.next is None:
        return root
    rest = reverse(root.next)
    
    root.next.next =root
    root.next =None
    return rest

#delete from perticular position
def deletelist(head, position):
    temp = head
    prev = head
    for i in range(0, position):
        if i==0 and position==1:
            head= head.next
        else:
            if i== position-1 and temp is not None:
                prev.next =temp.next
            else:
                prev= temp
                if prev is None:
                    break
                temp = temp.next
    return head
    
    
def display(root):
    while(root != None):
        print(root.data,end="")
        root=root.next

def arrtolist(arr, n):
    root=None
    for i in range(0,n,1):
        root =insert(root,arr[i])
    return root

if __name__=='__main__':
    arr=[1,2,3,4,5]
    n = len(arr)
    root=arrtolist(arr, n)
    real=root
    display(root)
    print("reversed")
    #root=reverse(real)
    root = deletelist(real,2)
    display(root)