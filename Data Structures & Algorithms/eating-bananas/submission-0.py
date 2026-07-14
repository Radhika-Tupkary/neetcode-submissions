class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        left, right = 1, max(piles)

        while left <= right:
            mid = (left+right) // 2
            # if mid == 0: 
            #     left = 1
            #     continue
            hrs = 0
            for pile in piles:
                remainder = 0 if pile % mid == 0 else 1
                hrs += (pile//mid) + remainder
            if hrs > h:
                left = mid + 1
            else:
                right = mid - 1
        
        return left