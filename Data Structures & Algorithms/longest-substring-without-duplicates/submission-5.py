class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength, i = 0, 0
        visited = {}

        for j in range(len(s)):
            if s[j] in visited and visited[s[j]] >= i:
                i = visited[s[j]] + 1
            
            visited[s[j]] = j
            maxLength = max(maxLength, j - i + 1)

        return maxLength