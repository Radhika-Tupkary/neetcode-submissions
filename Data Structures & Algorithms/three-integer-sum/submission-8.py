class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        if nums[0] > 0:
            return []
        elif nums[-1] < 0:
            return []
        else:
            for index, num in enumerate(nums):
                i = index + 1
                j = len(nums)-1
                target = 0 - num
                if index > 0 and nums[index] == nums[index-1]:
                    continue
                while i < j:
                    curr_sum = nums[i] + nums[j]
                    if curr_sum == target:
                        result.append([num, nums[i], nums[j]])
                        while i < j and nums[i] == nums[i+1]:
                            i += 1
                        # while i < j and nums[j] == nums[j-1]:
                        #     j -= 1
                        
                        i += 1
                        j -= 1

                    elif curr_sum < target:
                        i += 1
                    else:
                        j -= 1

        return result


                    
