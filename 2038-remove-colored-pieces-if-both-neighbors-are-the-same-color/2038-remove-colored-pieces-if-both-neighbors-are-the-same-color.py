class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        alice = 0
        bob = 0
        
        for i in range(2,len(colors)):
            if colors[i] == colors[i-1] == colors[i-2]:
                alice += 1 if colors[i] == "A" else 0
                bob += 1 if colors[i] == "B" else 0
        
        return alice > bob