class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start: int):
            if start == len(nums) - 1:
                result.append(nums[:])
            else:
                for i in range(start, len(nums)):
                    # swap elements
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)
        return result
