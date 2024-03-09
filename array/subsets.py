class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []

        sets = []
        subsets = []

        def dfs(index):
            if index >= len(nums):
                sets.append(subsets[:])
                return

            subsets.append(nums[index])
            dfs(index + 1)

            subsets.pop()
            dfs(index + 1)

        dfs(0)
        return sets
