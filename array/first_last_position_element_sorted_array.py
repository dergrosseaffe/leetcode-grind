class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findStartIndex(left: int, right: int) -> int:
            index = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

                if nums[mid] == target:
                    index = mid

            return index

        def findEndIndex(left: int, right: int) -> int:
            index = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

                if nums[mid] == target:
                    index = mid

            return index


        l = len(nums) - 1
        return [findStartIndex(0, l), findEndIndex(0, l)]
