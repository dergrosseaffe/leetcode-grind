class TimeMap:

    def __init__(self):
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""

        values = self.store[key]
        left, right = 0, len(values) - 1

        while left <= right:
            mid = left + (right - left) // 2

            currTimestamp, value = values[mid]
            if currTimestamp == timestamp:
                return value
            elif currTimestamp < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        return "" if right < 0 else values[right][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
