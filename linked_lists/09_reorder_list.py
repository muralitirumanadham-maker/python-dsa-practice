class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        if head is None or head.next is None:
            return head

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow.next
        slow.next = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


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

print("Original List:")
print_linked_list(head)

solution = Solution()
solution.reorderList(head)

print("\nReordered List:")
print_linked_list(head)

