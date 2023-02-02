class Solution:
    def numberOfWays(self, s: str) -> int:
        answer=0
        ans0=ans1 = 0
        preZero=preOne=0
        one=zero=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                ans0+=one*preZero
                answer+=ans0
                preZero+=1
                one=0
                zero+=1
            else:
                ans1+=zero*preOne
                answer+=ans1
                preOne+=1
                zero=0
                one+=1
        return answer
            