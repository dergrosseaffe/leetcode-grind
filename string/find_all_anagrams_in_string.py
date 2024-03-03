class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if (len(p) > len(s)): return []

        pc = [0] * 26
        sc = [0] * 26

        for i in range(len(p)):
            pc[ord(p[i]) - ord('a')] += 1
            sc[ord(s[i]) - ord('a')] += 1

        result = []
        if pc == sc:
            result.append(0)

        for i in range(len(p), len(s)):
            window_start = i - len(p)
            sc[ord(s[window_start]) - ord('a')] -= 1   # remove previous window char
            sc[ord(s[i]) - ord('a')]     += 1   # count current window char

            if sc == pc:
                result.append(window_start + 1)

        return result
