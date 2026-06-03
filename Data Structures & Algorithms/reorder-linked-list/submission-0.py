# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = f = head
        

        while f and f.next:
            s, f = s.next, f.next.next

        
        list1 = head
        list2 = self.reverseList(s.next)
        s.next = None

        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1

            list1 = temp1
            list2 = temp2


        

    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev



        



        