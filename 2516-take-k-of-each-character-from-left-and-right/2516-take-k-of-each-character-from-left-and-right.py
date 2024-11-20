class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total_freq = Counter(s)
        if total_freq["a"] < k or total_freq["b"] < k or total_freq["c"] < k:
            return -1
        
        freq = defaultdict(int)
        left = 0
        max_length = 0
        for right in range(len(s)):
            
            freq[s[right]] += 1
            
            while total_freq[s[right]] - freq[s[right]] < k:
                
                freq[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return len(s)-max_length