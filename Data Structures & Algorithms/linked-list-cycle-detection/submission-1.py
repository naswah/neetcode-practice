# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False;

        tail = head;
        while (tail and tail.next):
            head= head.next;
            tail = tail.next.next;

            if (head == tail):
                return True;
        
        return False;
