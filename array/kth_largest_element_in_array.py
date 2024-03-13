class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # partitions in descending order
        def partition3(nums, left, right):
            pivot_index = random.randint(left, right)
            nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
            pivot = nums[left]

            i, m1, m2 = left, left, right
            while i <= m2:
                if nums[i] > pivot:  # Greater elements moved to the left
                    nums[i], nums[m1] = nums[m1], nums[i]
                    m1 += 1
                    i += 1
                elif nums[i] < pivot:  # Lesser elements moved to the right
                    nums[i], nums[m2] = nums[m2], nums[i]
                    m2 -= 1
                else:
                    i += 1

            return m1, m2


        def quickselect(nums: List[int], left: int, right: int, k: int) -> int:
            if left <= right:

                m1, m2 = partition3(nums, left, right)

                if k < m1:  # checks left partition, where k is
                    return quickselect(nums, left, m1 - 1, k)
                elif k > m2:    # checks right partition, where k is
                    return quickselect(nums, m2 + 1, right, k)
                else:
                    return nums[k] # found


        # k-1 as k is 0-indexed
        return quickselect(nums, 0, len(nums) - 1, k - 1)
