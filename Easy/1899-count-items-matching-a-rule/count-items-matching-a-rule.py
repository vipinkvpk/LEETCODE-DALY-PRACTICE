class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            index = 0 
        elif ruleKey == "color":
            index = 1
        else:
            index=2
        matching_count =0 
        for item in items:
            if item[index]  == ruleValue:
                matching_count+=1 
        return matching_count
        
        