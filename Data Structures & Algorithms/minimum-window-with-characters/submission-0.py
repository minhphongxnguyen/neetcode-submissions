class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        freq_t = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(freq_t)
        res, res_len = [-1, -1], float('inf')
        

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in freq_t and window[c] == freq_t[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                c = s[l]
                window[c] -= 1
                if c in freq_t and window[c] < freq_t[c]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""



                


            





        


        