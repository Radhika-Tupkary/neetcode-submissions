class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = tokens[0]
        
        for token in tokens:
            if token not in "+-*/":
                stack.append(token)
            else:
                second = stack.pop()
                first = stack.pop()

                if token == "/":
                    result = int(int(first) / int(second))
                elif token == "+":
                    result = int(first) + int(second)
                elif token == "-":
                    result = int(first) - int(second)
                elif token == "*":
                    result = int(first) * int(second)

                stack.append(str(result)) 
            

        return int(result)
        