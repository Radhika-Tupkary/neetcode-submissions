class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        n = len(s)
        result = 0
        j = 0

        for i in range(n):
            counter[s[i]] = counter.get(s[i], 0) + 1
            most_freq_char_frequency = sorted(counter.items(), key=lambda x:x[1], reverse=True)[0][1]
            length_of_the_substring = (i + 1 - j)
            replacements = length_of_the_substring - most_freq_char_frequency

            if replacements > k:

                while replacements > k:
                    counter[s[j]] -= 1
                    j += 1
                    most_freq_char_frequency = sorted(counter.items(), key=lambda x:x[1], reverse=True)[0][1]
                    length_of_the_substring = (i + 1 - j)
                    replacements = length_of_the_substring - most_freq_char_frequency
            
            result = max(result, length_of_the_substring)

        return result

        