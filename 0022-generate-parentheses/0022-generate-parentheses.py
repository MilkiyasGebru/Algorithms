class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        answer = set()
        def backTrack(array,left,right):
            if (left < 0 or right < 0) or (right < left):
                return
            elif left == 0 and right == 0:
                nonlocal answer
                answer.add("".join(array))
                return
            else:
                backTrack(array+["("],left-1,right)
                backTrack(array+[")"],left,right-1)
        backTrack([],n,n)
        return answer