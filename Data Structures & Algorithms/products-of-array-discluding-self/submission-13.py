class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        res[0] = nums[0]
        for i in range(1, n):
            res[i] = nums[i] * res[i-1]
        
        res[n-1] = res[n-2]

        postfix = nums[n-1]

        for i in range(n-2, 0, -1):
            res[i] = res[i-1] * postfix
            postfix = postfix * nums[i]

        res[0] = postfix

        return res