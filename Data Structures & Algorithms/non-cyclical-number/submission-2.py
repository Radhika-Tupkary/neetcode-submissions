class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)

        # The sequence of sums of squared digits is guaranteed to eventually cycle (either reaching 1 or entering a loop)

        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)

        return True if fast == 1 else False

    def sumOfSquares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit * digit
            output += digit
            n = n // 10
        return output