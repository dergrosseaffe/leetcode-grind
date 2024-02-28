class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums: return []

        sumOfNTerms = (1 + len(nums))*len(nums)//2

        for n in nums:
            sumOfNTerms -= n

        return sumOfNTerms
