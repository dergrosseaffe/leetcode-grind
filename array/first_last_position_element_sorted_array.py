class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def rangeBinarySearch(left: int, right: int) -> List[int]:
            if left == right: return [-1, -1]

            middle = left + (right - left) // 2

            if nums[middle] == target:
                left = right = middle

                # expand search left
                while left > 0 and nums[left-1] == target:
                    left -= 1

                # expand search right
                while right < len(nums) - 1 and nums[right+1] == target:
                    right += 1

                return [left, right]
            elif nums[middle] > target:
                return rangeBinarySearch(left, middle)
            else:
                return rangeBinarySearch(middle + 1, right)

        return rangeBinarySearch(0, len(nums))
