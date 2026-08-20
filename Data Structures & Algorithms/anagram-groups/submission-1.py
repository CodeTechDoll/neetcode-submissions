class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = defaultdict(list)
        for st in strs:
            count = [0] * 26
            for c in st:
                count[ord(c) - ord('a')] += 1
            grams[tuple(count)].append(st)

        return list(grams.values())