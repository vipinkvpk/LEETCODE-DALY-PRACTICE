class Solution:
    def fillCups(self, amount: List[int]) -> int:
        total = sum(amount)
        max_cup = max(amount)
        return max(max_cup, (total+1)//2)
        