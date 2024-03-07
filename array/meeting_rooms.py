class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals) - 1):
            _, b = intervals[i]
            na, _ = intervals[i + 1]

            if b > na: return False

        return True
