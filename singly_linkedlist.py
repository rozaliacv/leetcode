class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBeg(self,data):
        if(self.head == None):
            self.head = Node(data)
            self.head.next = None
        else:
            old_head = self.head
            self.head = Node(data)
            self.head.next = old_head

    def insertAtEnd(self,data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
        else:
            itr = self.head
            while (itr.next!=None):
                itr = itr.next
            itr.next = new_node

    def insertAtIndex(self,data,indx):
        if(indx==0):
            self.insertAtBeg(data)
            return
        i = 0
        itr = self.head
        while (i<indx-1 and itr.next!=None):
            itr = itr.next
            i+=1
        
        
        new_node = Node(data)
        new_node.next = itr.next
        itr.next = new_node
         

    def deleteFromBeg(self):
        self.head = self.head.next
    
    def deleteFromEnd(self):
        if(self.head == None):
            return
        else:
            itr = self.head
            while (itr.next!=None):
                pre_itr = itr
                itr = itr.next
            pre_itr.next = None
    
    def deleteFromIndex(self,indx):
        if(indx==0):
            self.deleteFromBeg()
            return
        i = 0
        itr = self.head
        while (i<indx-1 and itr.next!=None):
            itr = itr.next
            i+=1
        
        del_node = itr.next
        itr.next = del_node.next
        

    def printList(self):
        itr = self.head
        while (itr.next!=None):
            print(itr.data,"-->",end="")
            itr = itr.next
        print(itr.data)

    
ll = LinkedList()
