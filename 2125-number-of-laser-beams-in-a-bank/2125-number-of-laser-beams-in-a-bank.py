class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        answer = 0
        prev = 0
        
        for i in range(len(bank)):
            lasers = bank[i].count("1")
            answer += lasers*prev
            prev = lasers if lasers != 0 else prev
        return answer