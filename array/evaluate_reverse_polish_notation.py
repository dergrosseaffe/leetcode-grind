class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = {
            '+': lambda a, b: b + a,
            '-': lambda a, b: b - a,
            '*': lambda a, b: b * a,
            '/': lambda a, b: int(b / a)
        }

        for token in tokens:
            if token in operators:
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(operators[token](a, b))
            else:
                stack.append(int(token))

        return stack.pop()
