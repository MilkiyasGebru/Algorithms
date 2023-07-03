class Solution:
    def compare(self,s,goal):
        diff = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff += 1
        
        return diff == 2
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        return  Counter(s) == Counter(goal) and (self.compare(s,goal) or (s == goal and max(Counter(s).values())>1))