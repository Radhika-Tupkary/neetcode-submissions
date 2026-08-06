class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)

        zeroPresent = False
        product = 1
        for num in nums:
            if num == 0:
                zeroPresent = True
                continue
            product = product * num 
        
        result = []

        for num in nums:
            if zeroPresent:
                if num != 0:
                    result.append(0)
                else:
                    result.append(product)
            else:
                result.append(product//num)

        return result