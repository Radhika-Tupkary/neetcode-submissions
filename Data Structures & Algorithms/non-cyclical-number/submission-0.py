class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            numStr = str(n)
            total = 0
            for s in numStr:
                total = total + int(s)*int(s)

            n = total

            if n == 1:
                return True
            
            if n in seen:
                return False

            seen.add(n)
            
        return True
        