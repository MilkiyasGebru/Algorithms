class Solution:
    def minimumPushes(self, word: str) -> int:
        total_count = 0 
        f = Counter(word)
        arr = sorted(f.values(),reverse=True)
        
        press = 1
        count = 8
        for value in arr:
            total_count += press*value
            count -= 1
            if count == 0:
                count = 8
                press += 1
        return total_count
            
        
        