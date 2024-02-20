class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}

        for c in magazine:
            counter[c] = counter.get(c, 0) + 1

        for c in ransomNote:
            if c not in counter or counter[c] == 0:
                return False
            counter[c] -= 1

        return True
