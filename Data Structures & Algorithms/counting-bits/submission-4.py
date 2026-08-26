class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)
        output[0] = 0

        for i in range(1, n+1):
            quotient = i // 2
            output[i] = output[quotient] + i % 2

        return output
        