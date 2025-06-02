

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         mainlist=[]
#         itr = list1
#         while(itr!=None):
#             mainlist.append(itr.val) 
#             itr = itr.next

#         itr = list2
#         while(itr!=None):
#             mainlist.append(itr.val) 
#             itr = itr.next
#         mainlist.sort()

        
#         ll = LinkedList()
#         for i in mainlist:
#             if(mainlist.index(i)==0):
#                 ll.insertAtBeg(i)
#             else:
#                 ll.insertAtEnd(i)
#         ll.printList()

#         return ll.head.val   
            
            
# class LinkedList:

#     def __init__(self):
#         self.head = None
        
#     def insertAtBeg(self,data):
#         if(self.head == None):
#             self.head = ListNode(data)
#             self.head.next = None
#         else:
#             old_head = self.head
#             self.head = ListNode(data)
#             self.head.next = old_head


#     def insertAtEnd(self,data):
#         new_node = ListNode(data)
#         if(self.head == None):
#             self.head = new_node
#         else:
#             itr = self.head
#             while (itr.next!=None):
#                 itr = itr.next
#             itr.next = new_node


#     def printList(self):
#         itr = self.head
#         while (itr.next!=None):
#             print(itr.val,"-->",end="")
#             itr = itr.next
#         print(itr.val)

    
# list1 = LinkedList()
# list1.insertAtEnd(1)
# list1.insertAtEnd(2)
# list1.insertAtEnd(4)
# list2 = LinkedList()
# list2.insertAtEnd(1)
# list2.insertAtEnd(3)
# list2.insertAtEnd(4)
# ans = Solution().mergeTwoLists(list1.head,list2.head)
# print(ans)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val<list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2
        return head.next