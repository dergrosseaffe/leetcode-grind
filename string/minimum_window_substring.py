class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_dict = defaultdict(int)
        for char in t:
            t_dict[char] += 1

        formed, required = 0, len(t_dict.keys())
        left, right = 0, 0
        window_count = defaultdict(int)
        minimum_window = (float('inf'), left, right)

        while right < len(s):
            character = s[right]
            window_count[character] += 1

            if character in t_dict and window_count[character] == t_dict[character]:
                formed += 1

            # move left window when we reach a point where all chars in t_dict
            # belong to window
            while left <= right and formed == required:
                current_size = right - left
                if current_size < minimum_window[0]:
                    minimum_window = current_size, left, right

                character = s[left]
                window_count[character] -= 1

                if character in t_dict and window_count[character] < t_dict[character]:
                    formed -= 1

                left += 1

            right += 1

        size, left, right = minimum_window
        return s[left:right+1] if size != float('inf') else ''
