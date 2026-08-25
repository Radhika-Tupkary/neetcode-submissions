from decimal import Decimal

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = tokens[0]
        i = 0

        while i < len(tokens):
            if tokens[i] not in ("+", "-", "*", "/"):
                stack.append(tokens[i])
            else:
                second = stack.pop()
                first = stack.pop()
                # Use int division // for floor division and handle truncation toward zero
                if tokens[i] == "/":
                    result = int(int(first) / int(second))
                else:
                    # Directly calculate based on operator instead of using eval()
                    if tokens[i] == "+":
                        result = int(first) + int(second)
                    elif tokens[i] == "-":
                        result = int(first) - int(second)
                    elif tokens[i] == "*":
                        result = int(first) * int(second)
                stack.append(str(result))
            i += 1

        return int(result)
        