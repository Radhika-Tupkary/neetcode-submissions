class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def rob(i):
            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]

            cache[i] = max(nums[i] + rob(i+2), rob(i+1))
            return cache[i]

        return rob(0)
 