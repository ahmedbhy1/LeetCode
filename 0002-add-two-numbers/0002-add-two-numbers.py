# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        l = l3
        l3.val = (l1.val + l2.val)%10
        rest = (l1.val + l2.val)//10

        while True:
            if l1 != None:
                l1=l1.next
            if l2 != None:
                l2=l2.next

            v1=0
            v2=0
            if l1 == None and l2 == None :
                break
            if l1 == None:
                v2 = l2.val
            if l2 == None:
                v1 = l1.val
            if l1 != None and l2 != None:
                v1 = l1.val
                v2 = l2.val

            l4 = ListNode()
            l4.val = ( v1 + v2 + rest) % 10
            rest = ( v1 + v2 + rest) // 10
            l3.next = l4
            l3 = l3.next

        if rest:
            l4 = ListNode()
            l4.val = rest
            l3.next = l4
            
        return l
        