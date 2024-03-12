class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bits = [1] * (len(nums) + 1)

        for num in nums:
            if bits[num]:
                bits[num] = 0
            else:
                return num
