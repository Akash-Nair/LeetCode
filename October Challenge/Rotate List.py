# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        
        if not head.next:
            return head
        
        length = 1
        
        h1 = head
        while h1.next:
            h1 = h1.next
            length += 1
            
        k = k%length
        print(length)
        if k == 0:
            return head
        
        first = head
        second = head
        
        for i in range(k):
            first = first.next
            
        while first.next:
            second = second.next
            first = first.next
            
        new_head = second.next
        second.next = None
        first.next = head
        
        return new_head
