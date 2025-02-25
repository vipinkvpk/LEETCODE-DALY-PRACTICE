class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res=""
        words=s.split()
        tr=words[:k]
        res+=" ".join(tr)
        return res
