class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack -- (value, index)
        # keep popping till value is greater than stack[1] and stack not empty
        result = [0] * len(temperatures)
        stack = []

        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                curr_value, curr_index = stack.pop()
                result[curr_index] = i - curr_index
            stack.append((val, i))
            
        return result
                


        