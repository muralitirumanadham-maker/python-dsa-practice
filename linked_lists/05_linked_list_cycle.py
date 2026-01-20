class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def create_cycle(head, pos):
    if pos == -1:
        return head

    cycle_node = None
    current = head
    index = 0

    while current.next:
        if index == pos:
            cycle_node = current
        current = current.next
        index += 1

    current.next = cycle_node
    return head


values = [1, 2, 3, 4, 5]
head = create_linked_list(values)
head = create_cycle(head, 2)

solution = Solution()
print(solution.hasCycle(head))

