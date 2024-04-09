class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        airports = defaultdict(list)

        for city_from, city_to, price in flights:
            airports[city_from].append((city_to, price))

        queue = deque()
        queue.append((src, 0, -1))

        min_price = float('+inf')
        visited = defaultdict(lambda: float('+inf'))

        while queue:
            city_from, current_cost, num_stops = queue.popleft()

            if num_stops > k:
                continue

            if city_from == dst:
                min_price = min(min_price, current_cost)
                continue

            for city_to, price in airports[city_from]:
                updated_cost = current_cost + price
                if updated_cost < min_price and updated_cost < visited[city_to]:
                    visited[city_to] = updated_cost
                    queue.append((city_to, updated_cost, num_stops + 1))

        return min_price if min_price != float('+inf') else -1
