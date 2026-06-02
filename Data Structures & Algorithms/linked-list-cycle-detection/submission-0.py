# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        l, r = head, head.next

        while r and r.next:
            if l == r:
                return True

            l = l.next
            r = r.next.next


            


        return False
        