# How do you find the length of a singly linked list? (solution)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_length(head):
    length = 0
    current = head
    
    while current:
        length += 1
        current = current.next
    
    return length

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original linked list:")
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

length = find_length(head)
print("\nLength of the linked list:", length)
