# class Solution:
#     def climbStairs(self, n: int) -> int:
#         cache = {}

#         def numOfWays(i):
#             if i == n:
#                 return 1

#             if i > n:
#                 return 0

#             if i in cache:
#                 return cache[i]

#             cache[i] = numOfWays(i + 1) + numOfWays(i + 2)

#             print(cache)

#             return cache[i]

#         return numOfWays(0)

class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        target = 1
        targetMinusOne = 1

        i = n-2

        while i >= 0:
            temp = targetMinusOne
            targetMinusOne = targetMinusOne + target
            target = temp
            i = i-1

        return targetMinusOne


