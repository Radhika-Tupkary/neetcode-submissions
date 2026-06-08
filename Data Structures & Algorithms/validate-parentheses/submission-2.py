class Solution:
    def isValid(self, s: str) -> bool:
        # implement stack

        dict_br = {'(':')', '{':'}', '[':']'}

        res = []

        for br in s:
            if br in dict_br:
                res.append(br)
            else:
                if len(res) == 0:
                    return False
                top = res.pop()
                if dict_br[top] != br:
                    return False

        return True if not res else False

        # time complexity - O(n)
        # space complexity - O(n)

        