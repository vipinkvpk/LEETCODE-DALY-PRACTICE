class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # from collections import Counter
        # freq_pattern=Counter(pattern)
        # freq_s=Counter(s)
        # for ch in pattern:
        #     for st in s:
        #         if freq_pattern[ch]==freq_s[st]:
        #             return True 
        #         return False

        ws = s.split()
        if len(pattern) != len(ws):
            return False
        d1={}
        d2={}

        for a,b in zip(pattern, ws):
            if (a in d1 and d1[a] !=b) or (b in d2 and d2[b] !=a):
                return False 
            d1[a]=b
            d2[b]=a
        return True
        