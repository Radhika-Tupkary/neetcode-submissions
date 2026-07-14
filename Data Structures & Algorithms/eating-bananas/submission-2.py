class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        left, right = 1, max(piles)

        while left <= right:
            mid = (left+right) // 2

            hrs = 0
            for pile in piles:
                remainder = 0 if pile % mid == 0 else 1
                hrs += (pile//mid) + remainder
            if hrs > h:
                left = mid + 1
            else:
                right = mid - 1
        
        return left