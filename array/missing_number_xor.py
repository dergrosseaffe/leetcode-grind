class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums: return []

        missing = len(nums)
        for i, n in enumerate(nums):
            missing ^= i ^ n # XOR on index and value

        return missing
