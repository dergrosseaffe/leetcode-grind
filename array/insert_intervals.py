class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []]
        nia, nib = newInterval
        n = len(intervals)
        i = 0

        while i < n and intervals[i][1] < nia:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= nib:
            nia = min(nia, intervals[i][0])
            nib = max(nib, intervals[i][1])
            i += 1

        result.append([nia, nib])

        while i < n:
            result.append(intervals[i])
            i += 1

        return result
