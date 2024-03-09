class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        options = []


        def backtrack(index, current):
            if current > target:
                return

            if current == target:
                result.append(options[:])
                return

            for i in range(index, len(candidates)):
                options.append(candidates[i])
                backtrack(i, current + candidates[i])
                options.pop()


        backtrack(0, 0)
        return result
