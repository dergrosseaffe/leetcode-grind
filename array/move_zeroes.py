class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        no_zeroes_left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[no_zeroes_left], nums[i] = nums[i], nums[no_zeroes_left]
                no_zeroes_left += 1
