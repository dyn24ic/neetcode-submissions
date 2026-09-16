class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toTuple(s: str):
            res = ([0] *26)
            for c in s:
                res[ord(c)-ord('a')] += 1
            return tuple(res)

        res = defaultdict(list)
        for s in strs:
            k = toTuple(s)
            res[k].append(s)

        return list(res.values())
