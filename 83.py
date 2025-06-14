# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        cur=head
        while(cur!=None ):
            test = cur
            while(test.next!=None and test.val==test.next.val):
                test.next = test.next.next

            cur =test.next

        
        return head

        