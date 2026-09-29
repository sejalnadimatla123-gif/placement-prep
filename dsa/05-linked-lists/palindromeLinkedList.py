# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
       stack = []
       current = head

       while current:
        stack.append(current.val)
        current = current.next
       
       current = head
       while current:
        if current.val != stack.pop():
            return False
        current = current.next
       return True

        