class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}

        def rob(i):
            if i >= n:
                return 0

            if i == n-1:
                cache[i] = nums[i]
                return cache[i]

            if i in cache:
                return cache[i]

            cache[i] = max(nums[i] + rob(i+2), rob(i+1))
            return cache[i]

        return rob(0)
