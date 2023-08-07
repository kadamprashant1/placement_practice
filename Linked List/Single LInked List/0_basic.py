
class Node:
    #Creating a node
    def __init__(self, item):
        self.item = item
        self.next= None
    
class LinkedList:

    def __init__(self):
        self.head = None

    def pushAtFront(self,new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def inserAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must in Linked list")
            return
        
        #Create a new node & put in the data
        new_node = Node(new_data)
        #make next of new Node as next
        #of prev_node
        new_node.next = prev_node.next
        # make next of prev_node as new_node
        prev_node.next = new_node

    def insetAtLast(self, new_data):
        #create a new node
        #put in the data
        # set next as None
        new_node = Node(new_data)
        #check if linked list is empty, then make new node as head
        if self.head is None:
            self.head = new_node
            return
        # else traverse the list till the last node
        last = self.head
        while (last.next):
            last = last.next
        # change the next of last node
        last.next = new_node


        while Linked_list.head != None:
            print(Linked_list.head.item, end=" ")
            Linked_list.head = Linked_list.head.next


if __name__ == '__main__':
    #creating a object of LinkedList class
    Linked_list = LinkedList()

    #assifn item values
    Linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # connect Nodes
    Linked_list.head.next = second
    second.next= third

    #print the linked list item
    while Linked_list.head != None:
        print(Linked_list.head.item, end=" ")
        Linked_list.head = Linked_list.head.next
    print("\nafter performing push on 7")
    Linked_list.pushAtFront(7)
    while Linked_list.head != None:
            print(Linked_list.head.item, end=" ")
            Linked_list.head = Linked_list.head.next
    print("\nafter performing insertion after 2")  
    Linked_list.inserAfter(Linked_list.head.next ,6)  
    while Linked_list.head != None:
            print(Linked_list.head.item, end=" ")
            Linked_list.head = Linked_list.head.next
    print("\nLinked list afer adding 9 at end of linked list")
    Linked_list.insetAtLast(10)
    while Linked_list.head != None:
            print(Linked_list.head.item, end=" ")
            Linked_list.head = Linked_list.head.next

 