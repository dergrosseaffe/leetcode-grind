class Solution(object):
    def binary_search(self, nums, target, left, right):
        if (left > right):
            return -1
            
        middle = left + (right - left) / 2

        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            return self.binary_search(nums, target, left, middle - 1)
        else:
            return self.binary_search(nums, target, middle + 1, right) 

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums, target, 0, len(nums) - 1)
        