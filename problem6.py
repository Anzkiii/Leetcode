class Solution:
    def twoSum(self, nums, target: int):
        tmp = {}
        for i, num in enumerate(nums):
            if target - num in tmp:
                return [tmp[target - num], i]
            tmp[num] = i

print(Solution().twoSum([x for x in range(1, 10000)], target=19999))
