class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n: return []

        def backtrack(open, close, str, result):
            if open == 0 and close == 0:
                result.append(str)
                return

            if (open > 0):
                backtrack(open - 1, close, str + '(', result)

            if (close > open):
                backtrack(open, close - 1, str + ')', result)

        result = []
        backtrack(n, n, '', result)

        return result
