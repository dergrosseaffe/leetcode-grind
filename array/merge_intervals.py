class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = []
        a, b = intervals[0]
        for i in range(1, len(intervals)):
            na, nb = intervals[i]

            if b < na:
                result.append([a, b])
                a, b = na, nb
            else:
                a = min(a, na)
                b = max(b, nb)

        if ([a, b]) not in result:
            result.append([a, b])

        return result
