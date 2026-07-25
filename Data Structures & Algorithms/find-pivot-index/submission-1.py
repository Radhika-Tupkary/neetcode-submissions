class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, total = 0, sum(nums)
        n = len(nums)

        for i in range(n):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]

        return -1
            
        