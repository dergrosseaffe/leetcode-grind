class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for n in nums:
            count[n] += 1

        i = 0
        for c in range(3):
            for j in range(count[c]):
                nums[i] = c
                i += 1
