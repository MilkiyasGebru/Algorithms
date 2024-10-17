class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        freq = Counter(skill)
        answer = 0
        team_score = sum(skill)
        
        if team_score %(len(skill)//2) != 0 and len(skill) > 2:
            return -1
        team_score //= (len(skill)//2)
        
        for player in skill:
            if freq[player] == 0:
                continue
            team_mate = team_score - player
            freq[team_mate] -= 1
            freq[player] -= 1
            if freq[team_mate] < 0:
                return -1
            answer += team_mate * player
        return answer