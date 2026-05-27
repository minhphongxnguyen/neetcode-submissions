class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        top_k = []
        for n, f in freq.items():
            heapq.heappush(top_k, (f, n))
            if len(top_k) > k:
                heapq.heappop(top_k)

        return [n for _, n in top_k]