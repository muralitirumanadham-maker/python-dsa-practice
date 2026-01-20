class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        if head is None or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            kth = prev_group_end
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_start = prev_group_end.next
            next_group_start = kth.next

            prev = next_group_start
            curr = group_start

            while curr != next_group_start:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            prev_group_end.next = kth
            prev_group_end = group_start


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
k = 2
head = create_linked_list(values)

print("Original List:")
print_linked_list(head)

solution = Solution()
new_head = solution.reverseKGroup(head, k)

print("\nAfter Reversing in K Groups:")
print_linked_list(new_head)

