class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        curr_min = float('inf')
        for p in prices:
            curr_min = min(curr_min, p)
            ans = max(ans, p - curr_min)

        return ans



        