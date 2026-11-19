from _heapq import heapify
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        # use fast and slow pointer to spilt two sections
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow.next
        slow.next = None

        # reverse the second part
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        second = prev

        # merge
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        