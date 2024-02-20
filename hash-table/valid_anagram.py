class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1

        for c in t:
            if c not in counter:
                return False

            counter[c] -= 1
            if (counter[c] == 0):
                del counter[c]

        return len(counter) == 0
