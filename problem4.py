class Solution:
    def isPalindrome(self, x: int):
        lstNumber = list(str(x))
        lstNumber.reverse()
        if lstNumber == list(str(x)):
            return True
        return False

