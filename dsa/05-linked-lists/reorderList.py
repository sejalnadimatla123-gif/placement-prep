class Solution(object):
    def reorderList(self, head):
        # find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #split the list into 2 halves
        second = slow.next
        slow.next = None

        #reverse the second half
        prev = None
        current = second

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        second = prev
        
        # merge 2 halves alternately
        first = head

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next





        