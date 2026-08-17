# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:  
            curr=head
            prev=head
            while prev and prev.next is not None:
                curr=curr.next
                prev=prev.next.next
                
                if curr==prev:
                    return True

            return False       
                


        