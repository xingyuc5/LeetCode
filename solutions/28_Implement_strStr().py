class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Special case when needle is empty string
        if needle == "":
            return 0

        # Initialize counter and compute lengths
        s, n, m = 0, len(haystack), len(needle)

        # Sliding window and compare
        while s <= n - m:
            i = 0
            while i < m:
                if haystack[s+i] != needle[i]:
                    break
                i += 1
            if i == m:
                return s
            s += 1
        return -1
