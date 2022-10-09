# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = sum_list = ListNode(-1,None)
        total = 0
        carry_over = 0
        while(l1 is not None and l2 is not None):
            total = carry_over+l1.val+l2.val
            if total>9:
                total = total%10
                carry_over = 1
            else:
                carry_over = 0
                
            print(total)
            p1.next = ListNode(total,None)
            p1 = p1.next
            l1=l1.next
            l2=l2.next
            
        while(l1 is not None):
            total = l1.val + carry_over
            if total>9:
                total = total%10
                carry_over = 1
            else:
                carry_over = 0
            p1.next = ListNode(total,None)
            p1=p1.next
            l1=l1.next
            
        while(l2 is not None):
            total = l2.val + carry_over
            if total>9:
                total = total%10
                carry_over = 1
            else:
                carry_over = 0
            p1.next = ListNode(total,None)
            p1=p1.next
            l2=l2.next
        
        if carry_over==1:
            p1.next = ListNode(1,None)
        
        return sum_list.next
    
            
            
                
                