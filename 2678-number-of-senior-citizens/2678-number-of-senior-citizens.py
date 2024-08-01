class Solution:
    def countSeniors(self, details: List[str]) -> int:
        total = 0
        for detail in details:
            total += 1 if int(detail[11:13]) > 60 else 0
        return total