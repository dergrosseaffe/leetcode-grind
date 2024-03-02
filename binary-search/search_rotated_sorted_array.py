class Solution:


    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(left, right, key):
            if left > right:
                return -1

            mid = left + (right - left) // 2
            if nums[mid] == key:
                return mid

            if nums[left] <= nums[mid]: # left to mid is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else: # mid to right is sorted
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            return binarySearch(left, right, target)


        if not nums: return -1
        return binarySearch(0, len(nums) - 1, target)
