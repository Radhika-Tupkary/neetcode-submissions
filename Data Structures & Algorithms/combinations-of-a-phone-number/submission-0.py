class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToStr = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        n = len(digits)
        values = []
        
        for digit in digits:
            values.append(digitToStr[digit])

        # values = ["def", "ghi"]
        result = []

        def combine(i, curStr):
            if i == n:
                result.append(curStr)
                return
            
            for letter in values[i]:
                combine(i+1, curStr + letter)
            

        combine(0, "")
        return result