class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c) # accumulates number
            elif c == '[': # start of a repeating sequence
                stack.append(num)
                stack.append('#')
                num = 0
            elif c.isalpha():
                stack.append(c)
            elif c == ']': # retrieves repeating sequence
                seq = ''
                while stack[-1] != '#':
                    seq = stack.pop() + seq
                stack.pop()
                k = stack.pop()
                stack.append(seq*k)

        print(stack)
        return ''.join(stack)
