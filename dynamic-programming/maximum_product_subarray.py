class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        current_max = nums[0]
        current_min = nums[0]
        global_max  = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                current_min, current_max = current_max, current_min

            current_min = min(current_min * nums[i], nums[i])
            current_max = max(current_max * nums[i], nums[i])

            global_max  = max(global_max, current_max)

        return global_max
