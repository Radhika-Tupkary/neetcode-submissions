class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        targetSum = int((n * (n+1))/2)
        currSum = 0
        for el in nums:
            currSum += el
        return targetSum - currSum
        