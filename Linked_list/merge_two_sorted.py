# How to merge two sorted linked lists? (solution)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    # Create a dummy node to simplify the merging process
    dummy = ListNode(0)
    current = dummy
    
    # Iterate through both lists simultaneously
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Append remaining nodes from the non-empty list
    current.next = l1 if l1 else l2
    
    return dummy.next

# Example usage:
# Create two sorted linked lists: 1 -> 2 -> 4 and 1 -> 3 -> 4
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

print("First sorted linked list:")
current = l1
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

print("\nSecond sorted linked list:")
current = l2
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

merged_list = merge_two_lists(l1, l2)

print("\nMerged sorted linked list:")
current = merged_list
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
