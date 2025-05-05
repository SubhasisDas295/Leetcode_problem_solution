# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode() #listnode created as dummy
        current = dummy    # here current == dummy 
        carry = 0

        while l1 or l2 or carry:         # True     
            val1 = l1.val if l1 else 0   # 3
            val2 = l2.val if l2 else 0   # 4
            total = val1 + val2 + carry  # 3+4+1=8
            carry = total // 10          # 0
            digit = total % 10           # 8

            current.next = ListNode(digit) # 7->0->8
            current = current.next         # 7->0->8 as object

            if l1: l1 = l1.next           # None
            if l2: l2 = l2.next           # None

        return dummy.next


