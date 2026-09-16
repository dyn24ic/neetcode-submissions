class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            wordcount = defaultdict(int)
            for c in s:
                wordcount[c] += 1
            
            for c in t:
                if wordcount[c] <= 0:
                    return False
                else:
                    wordcount[c] -= 1

        return True
