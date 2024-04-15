class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = defaultdict(int)
        for task in tasks:
            task_counts[task] += 1

        max_heap = []
        for task, count in task_counts.items():
            heapq.heappush(max_heap, (-count, task))

        cycle = 0
        cooling_queue = deque()
        # ordering = []
        while max_heap or cooling_queue:
            cycle += 1

            if max_heap:
                count, task = heapq.heappop(max_heap)
                # ordering.append(task)

                if count < -1:
                    # add to queue for reprocessing at a later cycle
                    cooling_queue.append((count + 1, task, cycle + n))
            # else:
                # idles
                # ordering.append('Idle')


            # push ready tasks in the heap again
            if cooling_queue:
                count, task, ready_cycle = cooling_queue[0]
                if ready_cycle == cycle:
                    cooling_queue.popleft()
                    heappush(max_heap, (count, task))

        # print(ordering)
        return cycle
