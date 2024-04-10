class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        S, B, total_size = nums1, nums2, len(nums1) + len(nums2)
        if len(nums1) > len(nums2):
            S, B = B, S

        left, right = 0, len(S)

        while left <= right:
            partition_s = (left + right) // 2
            partition_b = (total_size + 1) // 2 - partition_s

            left_s  = float("-inf") if partition_s == 0 else S[partition_s - 1]
            right_s = float("inf") if partition_s == len(S) else S[partition_s]

            left_b  = float("-inf") if partition_b == 0 else B[partition_b - 1]
            right_b = float("inf") if partition_b == len(B) else B[partition_b]

            if left_s <= right_b and left_b <= right_s:
                if total_size % 2 == 0:
                    return (max(left_s, left_b) + min(right_s, right_b)) / 2
                else:
                    return max(left_s, left_b)
            elif left_s > right_b:
                right = partition_s - 1
            else:
                left = partition_s + 1
