class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = 0
        for num in nums:
            once ^= num

        return once
