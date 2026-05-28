class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        go through the string, anchor the char on the left pointer
        move the right pointer rightward, use replacement if it's different than the anchor
        if replacement runs out,

        replacement = 2
        AACBCA
        """
        ans = 0
        char_set = set(s)

        for c in char_set:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    
                    l += 1

                ans = max(ans, r - l + 1)

        return ans

                

        