class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordmap = defaultdict(list) # 26-tuple : List[str]
        for s in strs:
            res = [0] * (ord("z") - ord("a"))
            for c in s:
                res[ord(c) - ord("a")] += 1
            wordmap[tuple(res)].append(s)

        return list(wordmap.values())
