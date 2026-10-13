# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # right pointer move n steps forward
        for _ in range(n):
            right = right.next

        # right and left pointer move at a same speed until right pointer reach None
        while right:
            left = left.next
            right = right.next
        
        # skip the target node (remove)
        left.next = left.next.next

        # return head
        return dummy.next