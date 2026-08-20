class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = {}
        for st in strs:
            key = tuple(sorted(st))

            if key not in grams:
                grams[key] = []
            
            grams[key].append(st)           

        return list(grams.values())