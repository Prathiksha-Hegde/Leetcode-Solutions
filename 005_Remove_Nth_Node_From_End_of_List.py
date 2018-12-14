# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        list_values =[]
        while(head!= None):
            list_values.append(head.val)
            head= head.next 
        del list_values[-n]
        return list_values 