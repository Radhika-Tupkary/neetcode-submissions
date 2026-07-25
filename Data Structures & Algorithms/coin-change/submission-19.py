class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # base condition to stop recursion - 
        # 1. The amount is 0. 2. All the coins are greater than the amount.

        cache = {}

        def explore(amount):
            if amount == 0:
                return 0

            best = float('inf')

            if amount in cache:
                return cache[amount]

            for coin in coins:
                if coin <= amount:
                    ans = explore(amount - coin)
                    if ans != -1:
                        best = min(best, ans + 1)
            
            if best == float('inf'):
                cache[amount] = -1
                return -1

            cache[amount] = best

            return best
        
        return explore(amount)
        