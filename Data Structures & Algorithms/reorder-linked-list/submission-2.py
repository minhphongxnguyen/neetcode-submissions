# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        
        first, second = head, self.reverseList(slow.next)
        slow.next = None
        
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1

            first, second = temp1, temp2
        

    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev



        



        