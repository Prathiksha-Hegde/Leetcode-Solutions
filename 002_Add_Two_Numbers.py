# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = val
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_1 = self.getting_values_from_ll(l1)
        sum_2 = self.getting_values_from_ll(l2)
        result = sum_1 + sum_2
        final_ll = self.convert_sum_ll(result)
        return final_ll
    def getting_values_from_ll (self,l1):
        factor = 1
        sum_values = 0
        while(True):
            value = l1.val
            sum_values = sum_values + value*factor
            factor = factor *10
            if l1.next is None:
                break
            else:
                l1 = l1.next
        return sum_values
    def convert_sum_ll( self, result):
            ll = ListNode(None)
            start_node = ll
            while(True):
                rem = result % 10
                result = result /10
                ll.val = rem
                if (result != 0):
                    another_node = ListNode(None)
                    ll.next = another_node
                    ll = another_node
                else:
                    break
            return start_node
            
       
            
            