class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort based on end time so we always pick the earliest end time when overlaps occur
        intervals.sort(key=lambda x: x[1])

        to_remove = 0
        _, end = intervals[0]

        for start, current_end in intervals[1:]:
            if start < end:  # Overlap
                to_remove += 1
            else:
                # No overlap, so update end for comparison with next interval
                end = current_end

        return to_remove
