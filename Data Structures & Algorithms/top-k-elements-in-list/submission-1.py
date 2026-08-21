class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # assign frequencies of each element
        frequencies: dict[int, int] = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0 ) + 1
        # sort the collection based on frequency
        ordered = sorted(
            frequencies.items(),
            key=lambda pair: pair[1],
            reverse=True
        )
        # take top k
        result = []
        for pair in ordered[:k]:
            result.append(pair[0])

        return(result)