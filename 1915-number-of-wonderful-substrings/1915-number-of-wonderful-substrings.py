class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        
        '''
        Why I am given only 10 characters?
        using bitmanupulation I can easily check if its wonderful or not (n & n-1 ==0)
        And what is the advantage of substring?
        '''
        
        prefix = defaultdict(int)
        prefix[0] = 1
        value = total = 0
        
        for c in word:
            
            value ^= (1 << (ord(c)-ord("a")))
            for i in range(10):
                total += prefix[value ^ (1 << i)]
            total += prefix[value]   
            prefix[value] += 1
        
        return total
                
            
    