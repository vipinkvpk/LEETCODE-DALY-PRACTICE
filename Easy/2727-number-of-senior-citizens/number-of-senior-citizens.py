class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for s in details:
            s1= s[11:13]
            if int(s1)>60:
                count += 1
        return count
        