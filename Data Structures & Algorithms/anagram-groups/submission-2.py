class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c)-ord('a')] += 1

            anagram_group[tuple(freq)].append(s)

        return list(anagram_group.values())
        