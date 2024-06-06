class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        
        length = len(students[0])
        for i in range(len(students)):
            bit_value = 0
            for j in range(len(students[i])):
                if students[i][j]:
                    bit_value ^= (1 << j)
            students[i] = bit_value
        
        for i in range(len(mentors)):
            bit_value = 0
            for j in range(len(mentors[i])):
                if mentors[i][j]:
                    bit_value ^= (1 << j)
            mentors[i] = bit_value
        
        @cache
        def dp(i,bitmask):
            
            if i == len(students):
                return 0
            ans = -math.inf
            for j in range(len(students)):
                
                if (bitmask & ( 1 << j)) == 0:
                    ans = max(ans, length - bin((students[i] ^ mentors[j])).count("1") + dp(i+1,bitmask ^ ( 1 << j)))
            
            return ans
        
        return dp(0,0)
        