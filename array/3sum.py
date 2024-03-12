class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        S = set()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            complements = set()
            for j in range(i + 1, len(nums)):
                complement = -nums[i] - nums[j]
                if complement in complements:
                    triplet = (nums[i], nums[j], complement)
                    if triplet not in S:
                        S.add(triplet)

                complements.add(nums[j])

        return S
