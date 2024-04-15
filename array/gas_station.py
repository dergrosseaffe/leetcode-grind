class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)

        i = 0
        while i < l:
            start = i
            available = gas[i] - cost[i]

            while available >= 0:
                i = (i + 1) % l
                available += gas[i] - cost[i]
                if i == start:
                    return i

            if i < start:
                return -1
            i = i + 1

        return -1
