class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return chr(257)
        result = ''
        for string in strs:
            result += str(len(string)) + '#' + string

        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        if s == chr(257):
            return []
        result = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            result.append(s[j+1 : j+1+length])
            i = j + 1 + length
        print(result)
        return result