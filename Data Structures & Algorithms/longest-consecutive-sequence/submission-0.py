class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in num_set:
            if n - 1 in num_set:
                continue
            
            streak = 1
            while True:
                if n + streak not in num_set:
                   break
                
                streak += 1

                
            longest = max(longest, streak)

        return longest
                

        