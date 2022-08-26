import math
class Solution:
    def isPowerOfThree(self, n: int):
        numLimiter = 0
        while (3 ** numLimiter) <= n:
            if 3 ** numLimiter == n:
                return True
            numLimiter += 1
        return False
print(Solution().isPowerOfThree(27))

