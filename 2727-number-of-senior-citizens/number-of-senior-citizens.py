class Solution:
    def countSeniors(self, details: List[str]) -> int:

        return sum(1 for detail in details if int(detail[11]+detail[12])>60) 