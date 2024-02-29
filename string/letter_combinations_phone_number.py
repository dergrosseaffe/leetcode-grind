class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(current, path):
            if current == len(digits):
                combinations.append(''.join(path))
                return

            digit = digits[current]
            for char in dic[digit]:
                path.append(char)               # create a recursion path for the char
                backtrack(current + 1, path)
                path.pop()                      # remove char from recursion path

        combinations = []
        backtrack(0, [])
        return combinations
