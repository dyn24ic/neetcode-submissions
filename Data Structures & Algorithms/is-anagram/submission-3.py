from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        scount, tcount = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            scount[s[i]] = scount[s[i]] + 1
            tcount[t[i]] = tcount[t[i]] + 1
        return scount == tcount
        
        