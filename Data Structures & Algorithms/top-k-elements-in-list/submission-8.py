import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs: dict[int, int] = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        heap = []
        # heapq.heappeah(heap, (priority, value))
        for num, freq in freqs.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for _, num in heap]
        