class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    # Initialize a dummy node to simplify code logic
    dummy = ListNode()
    current = dummy
    carry = 0

    # Loop through both lists until both lists are exhausted
    while l1 or l2 or carry:
        # Get the current values, defaulting to 0 if the list is exhausted
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)

        # Calculate the new sum and carry over
        total = val1 + val2 + carry
        carry = total // 10
        new_val = total % 10

        # Create a new node with the sum's digit
        current.next = ListNode(new_val)
        current = current.next
        print(current)

        # Move to the next nodes in the lists
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # The dummy node's next points to the head of the resultant list
    return dummy.next
