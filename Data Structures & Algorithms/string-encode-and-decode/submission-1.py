class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")

        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        curr = 0
        while curr < len(s):
            j = s.index('#', curr)
            length = int(s[curr:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            curr = end
        return res





