class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # res=[]
        # list1=s1.split(" ")
        # list2=s2.split(" ")
        # for ch in list1:
        #     if ch not in list2:
        #         res.append(ch)
        # for ch1 in list2:
        #     if ch1 not in list1:
        #         res.append(ch1)
        # return res
        # s1.split(" ")
        # s2.split(" ")
        from collections import Counter
        count= collections.Counter((s1 + ' ' + s2).split())
        return [word for word,freq in count.items() if freq==1]