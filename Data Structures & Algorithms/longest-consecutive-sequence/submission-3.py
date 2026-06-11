# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         # 1. convert the nums into set
#         # 2. sort the array
#         # 3. sliding window

#         if not nums:
#             return 0

#         sorted_unique_nums = sorted(list(set(nums)))
#         window, maxWindow = 1, 1

#         for i in range(1,len(sorted_unique_nums)):
#             if (sorted_unique_nums[i]) - (sorted_unique_nums[i-1]) == 1:
#                 window += 1
#                 maxWindow = max(window, maxWindow)
#             else:
#                 window = 1

#         return maxWindow

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Start of a sequence
            if num - 1 not in num_set:
                length = 1

                while num + length in num_set:
                    length += 1

                longest = max(longest, length)

        return longest
