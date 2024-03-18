# How do you sort a linked list? (solution)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(left, right):
    # Create a dummy node to simplify merging
    dummy = ListNode()
    current = dummy

    # Merge the two sorted lists
    while left and right:
        if left.val <= right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    # Append remaining nodes, if any
    current.next = left if left else right

    return dummy.next

def sort_linked_list(head):
    if not head or not head.next:
        return head  # Base case: empty list or single node

    # Find the middle of the list
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Split the list into two halves
    right = slow.next
    slow.next = None

    # Recursively sort each half
    left_sorted = sort_linked_list(head)
    right_sorted = sort_linked_list(right)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

# Example usage:
# Create a linked list: 4 -> 2 -> 1 -> 3
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

print("Original linked list:")
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

# Sort the linked list
sorted_head = sort_linked_list(head)

print("\nSorted linked list:")
current = sorted_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
