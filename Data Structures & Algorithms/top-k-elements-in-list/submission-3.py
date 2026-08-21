class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # assign frequencies of each element
        # {num, frequency}
        frequencies: dict[int, int] = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0 ) + 1
        # sort the collection based on frequency
        ordered = sorted(
            frequencies,
            key=lambda num: frequencies[num],
            reverse=True
        )
        # take top k
        return ordered[:k]
        