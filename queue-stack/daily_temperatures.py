class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        greater_temperatures = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                greater_temperatures[index] = i - index

            stack.append(i)

        return greater_temperatures
