class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = nums[0]

        for index, max_jump in enumerate(nums):
            if farthest < index:    # stuck
                return False
            farthest = max(farthest, index + max_jump)
            if farthest >= len(nums) - 1:
                return True

        return False
