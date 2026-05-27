class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.extend([f"{len(s)}#"]+[c for c in s])

        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        curr = 0
        csubstr_metadata = []
        while curr < len(s):
            if s[curr] == '#':
                substr_len = int(''.join(csubstr_metadata))
                start = curr + 1
                end = start + substr_len
                res.append(s[start:end])
                curr = end
                csubstr_metadata = []
            else:
                csubstr_metadata.append(s[curr])
                curr += 1

        return res





