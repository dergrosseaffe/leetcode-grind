class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        prev_operation = '+'
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                current_number = current_number * 10 + int(char) if current_number != None else int(char)

            if char in "+-*/" or i == len(s) - 1:
                match prev_operation:
                    case '+':
                        stack.append(current_number)
                    case '-':
                        stack.append(-current_number)
                    case '*':
                        stack.append(stack.pop() * current_number)
                    case '/':
                        stack.append(int(stack.pop() / current_number))

                current_number = 0
                prev_operation = char

        return sum(stack)
