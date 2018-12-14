# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None):
            return head
          
        list_values = self.get_values_ll(head)
        a = (list(reversed(list_values)))
        print ("reversed_list =", a)
        final_ll = self.create_ll(a)
        return final_ll

    def get_values_ll (self, head):
        list_values =[]
       
        while(True):
            value = head.val
            list_values.append(value)
            if (head.next is None):
                break
            else:
                head = head.next
        return list_values
    
    def create_ll (self, a):
        ll = ListNode(None)
        start_node = ll
        length = len(a)
        iter_no = 0;
        for i in a:
            ll.val = i
            iter_no = iter_no +1;
            if iter_no != len(a):
                anothernode = ListNode(None)
                ll.next = anothernode
                ll = anothernode   
       
        return start_node
    
    