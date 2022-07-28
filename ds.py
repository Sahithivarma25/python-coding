class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printLL(self):
        if self.head==None:
            print("Linked list is empty!")
        else:
            n=self.head
            while n:
                print(n.data)
                n=n.next
    def add_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.next:
                n=n.next
            n.next=new_node
    def delete_begin(self):
        if self.head==None:
            print("Linked list is empty! so we cant delete nodes")
        else:
            self.head=self.head.next
    def delete_end(self):
        n=self.head
        while n.next.next:
            n=n.next
        n.next=None
l=LinkedList()
l.add_begin(10)
l.add_begin(20)
l.add_end(100)
l.delete_begin()
l.delete_end()
l.printLL()
