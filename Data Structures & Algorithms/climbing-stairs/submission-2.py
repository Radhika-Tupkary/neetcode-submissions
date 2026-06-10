class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def numOfWays(i):
            if i == n:
                return 1

            if i > n:
                return 0

            if i in cache:
                return cache[i]

            cache[i] = numOfWays(i + 1) + numOfWays(i + 2)

            return cache[i]

        return numOfWays(0)