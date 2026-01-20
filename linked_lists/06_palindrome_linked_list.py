class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


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


values = [1, 2, 3, 2, 1]
head = create_linked_list(values)

print("Linked List:")
print_linked_list(head)

solution = Solution()
print("\nIs Palindrome:")
print(solution.isPalindrome(head))

