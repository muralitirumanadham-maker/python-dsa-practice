class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        before = None
        temp = head

        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        return before


def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

print("Original Linked List:")
print_linked_list(head)

solution = Solution()
reversed_head = solution.reverseList(head)

print("\nReversed Linked List:")
print_linked_list(reversed_head)

