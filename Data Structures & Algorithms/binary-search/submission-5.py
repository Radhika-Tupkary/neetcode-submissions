# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l = 0
#         n = len(nums)
#         r = n-1

#         while l <= r:
#             middle = int((l+r)/2)
#             if nums[middle] == target:
#                 return middle
#             elif nums[middle] < target:
#                 l = middle + 1
#             else:
#                 r = middle - 1

#         return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def explore(i, j):
            if i > j:
                return -1
                
            middle = int((i+j)/2)
            
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                return explore(middle+1, j)
            else:
                return explore(i, middle-1)

            return -1
            

        return explore(0, len(nums)-1)