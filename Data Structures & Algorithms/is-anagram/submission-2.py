class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # approach 1 -- sort both strings and compare
        # approach 2 -- dictionary_1 {r:2, a:2, c:2, e:1}, dictionary_2 {c:2, a:2, r:2, e:1}
            # default_dict = {dict(int)}
                
        if len(s) != len(t):
            return False

        dictionary_1 = {}
        dictionary_2 = {}

        for i in s:
            if i not in dictionary_1:
                dictionary_1[i] = 1
            else:
                dictionary_1[i] += 1

        for i in t:
            if i not in dictionary_2:
                dictionary_2[i] = 1
            else:
                dictionary_2[i] += 1

        if len(dictionary_1) != len(dictionary_2):
            return False

        for i in dictionary_1:
            if i not in dictionary_2 or dictionary_1[i] != dictionary_2[i]:
                return False
        
        return True

    # time complexity - O(m+n)
    # space complexity - O(1) --- 26 different chars
