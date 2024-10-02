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

            l1=l1.next if l1 else l1
            l2=l2.next if l2 else l2
            
            v2=0
            if not l1 and not l2 :
                break
            v2 = 0 if l1 else l2.val
            v1 = 0 if l2 else l1.val     

            if l1 and l2:
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
        