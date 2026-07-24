class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums[1:])

        if leftSum == rightSum:
            return 0

        n = len(nums)

        for i in range(1, n):
            leftSum += nums[i-1]
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i

        return -1
            
        