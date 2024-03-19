# How do you reverse a singly linked list without recursion? (solution)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
         if head == None or head.next == None:
            return head
         prev, curr = None, head
         while curr:
               next_node = curr.next
               curr.next = prev
               prev = curr
               curr = next_node
         return prev
lis = [5,4,3,2,1]
hello = Solution()
print(" After reverse ",lis)