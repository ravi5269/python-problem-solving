# How do you reverse a linked list in place? (solution)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the link
        
        # Move pointers one step forward
        prev = current
        current = next_node
    
    return prev  # Return

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
    print(current.val, end=" , ")
    current = current.next
print("None")

# Reverse the linked list
reversed_head = reverse_linked_list(head)

print("Reversed linked list:")
current = reversed_head
while current:
    print(current.val, end=" ,")
    current = current.next
print("None")
