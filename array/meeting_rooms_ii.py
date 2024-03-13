class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []

        intervals.sort(key=lambda x: x[0])
        rooms = 1
        heapq.heappush(heap, intervals[0][1])

        for (start, end) in intervals[1:]:
            first_to_finish = heap[0]   # peek element
            if start < first_to_finish: # we need another room
                rooms += 1
            else:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

        return rooms
