class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        # since strings are immutable, this will result in a lot of allocations so eventually
        # we should accumulate pieces into a list and eventually use "".join(pieces)
        for s in strs:
            # find current string length and add it on
            res += str(len(s))
            res  += "#"
            # add the string onto the result
            res += s

        return res

    def decode(self, s: str) -> List[str]:
        result: List[str] = []
        i = 0
        while i < len(s):
            # find j = position of next "#"
            j = i
            while s[j] != "#":
                j += 1
            # parse s[i:j] as integer length
            length = int(s[i:j])
            # extract exactly that many chars after j
            start = j + 1
            end = start + length
            decoded = s[start:end]
            # append extracted string
            result.append(decoded)
            # move i past extracted string
            i = end
        return result