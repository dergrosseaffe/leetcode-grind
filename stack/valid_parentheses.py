class Solution(object):
    def isValid(self, s):
        valid_pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for char in s:
            if char in valid_pairs:
                stack.append(valid_pairs[char])
            elif not stack or stack.pop() != char:
                return False

        return not stack