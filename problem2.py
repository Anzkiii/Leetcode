
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode):
        palindromeValues = []
        while head:
            palindromeValues.append(head.val)
            head = head.next
        left, right = 0, len(palindromeValues) - 1
        while left <= right:
            if palindromeValues[left] != palindromeValues[right]:
                return False
            left += 1
            right -= 1
        return True
    


