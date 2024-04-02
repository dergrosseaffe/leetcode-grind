class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stops = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                stops[stop].append(bus)

        if target not in stops:
            return -1

        queue = deque()
        for bus in stops[source]:
            queue.append((bus, 1))

        visited_buses = set()
        visited_stops = set()
        while queue:
            bus_id, taken = queue.popleft()

            if target in routes[bus_id]:
                return taken
            else:
                for stop in routes[bus_id]:
                    if stop not in visited_stops:
                        for bus in stops[stop]:
                            if bus not in visited_buses and bus != bus_id:
                                queue.append((bus, taken + 1))
                        visited_stops.add(stop)

            visited_buses.add(bus_id)

        return -1
