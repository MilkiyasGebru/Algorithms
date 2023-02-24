class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        answer = [0 for _ in range(k)]
        f = defaultdict(set)
        
        for user,time in logs:
            f[user].add(time)
        
        for key in f.keys():
            answer[len(f[key])-1] += 1
        return answer