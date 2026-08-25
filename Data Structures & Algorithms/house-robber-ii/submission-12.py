class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_range(start, end):
            cache = {}

            def rob(i):
                if i > end:
                    return 0

                if i in cache:
                    return cache[i]

                cache[i] = max(nums[i] + rob(i+2), rob(i+1))
                return cache[i]
            
            return rob(start)

        case1 = rob_range(1, n-1)
        case2 = rob_range(0, n-2)

        return max(case1, case2)
        