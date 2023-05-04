class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        f=defaultdict(int)
        
        for i in range(len(senate)):
            f[senate[i]]+=1
            
        q=deque(senate)
        ban=defaultdict(int)
        
        while(f["R"]>0 and f["D"]>0):
            if q[0]=="R" and ban["R"]==0:
                ban["D"]+=1
                q.append(q.popleft())
            elif q[0]=="R":
                ban["R"]-=1
                q.popleft()
                f["R"]-=1
            elif q[0]=="D" and ban["D"]==0:
                ban["R"]+=1
                q.append(q.popleft())
            else:
                ban["D"]-=1
                f["D"]-=1
                q.popleft()
        return "Radiant" if f["R"]>f["D"] else "Dire"        