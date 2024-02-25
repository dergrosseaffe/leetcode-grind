class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = strs[0]

        for s in strs:
            if s == commonPrefix: continue

            for i in range(len(commonPrefix)):
                min_len = min(len(s), len(commonPrefix))
                while i < min_len and s[i] == commonPrefix[i]:
                    i += 1
                commonPrefix = commonPrefix[:i]
                if not commonPrefix:
                    break

        return commonPrefix
