class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}

        for string in strs:
            n = len(string)
            if n not in result_dict:
                result_dict[n] = [[string]]
            else:
                found = False
                curr_list = result_dict[n]
                for i in range(len(result_dict[n])):
                    first = result_dict[n][i][0]
                    if sorted(first) == sorted(string):
                        found = True
                        result_dict[n][i].append(string)
                        break
                if not found:
                    result_dict[n].append([string])

        result = []
        for k, v in result_dict.items():
            result.extend(v)

        return result