class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "-", "*", "/"]
        stack = []

        for t in tokens:
            if t not in operands:
                stack.append(int(t))
            else:
                a, b = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(b + a)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(b * a)
                elif t == "/":
                    stack.append(int(float(b) / a))

        print(stack)

        return stack[0]