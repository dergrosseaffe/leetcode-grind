class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums) # use a set for faster lookups

        longest = 0
        for k in d:
            # is start of a sequence?
            if k-1 not in d:
                # count sequences
                i = 1
                while k+i in d:
                    i += 1
                longest = max(i, longest)

        return longest
