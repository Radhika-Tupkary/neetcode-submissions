class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. binary search to find the minimum element in the array
        # 2. binary seach again to find the target if not found already

        l, r = 0, len(nums)-1
        pivot = 0
        if nums[l] > nums[r]:
            while l <= r:
                m = (l+r) // 2
                if nums[m] == target:
                    return m
                if nums[m] >= nums[0]:
                    l = m+1
                else:
                    pivot = m
                    r = m-1
            pivot = l
        
        if target >= nums[pivot] and target <= nums[-1]:
            listWithTarget = nums[pivot:]
            initialPtr = pivot
        else:
            listWithTarget = nums[:pivot]
            initialPtr = 0
        
        l, r = 0, len(listWithTarget)-1

        result = -1

        while l <= r:
            m = (l+r) // 2
            if listWithTarget[m] == target:
                result = m + initialPtr
                break
            if listWithTarget[m] < target:
                l = m+1
            else:
                r = m-1

        return result