class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = Counter(s)
        for c in t:
            if c not in s_freq:
                return False

            s_freq[c] -= 1

        return all(f == 0 for f in s_freq.values())


        