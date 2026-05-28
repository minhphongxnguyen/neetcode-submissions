class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        l = 0

        for r, c in enumerate(s):
            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            seen[c] = r
            longest = max(longest, r - l + 1)

        return longest


        