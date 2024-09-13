class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        prefix = [[0 for _ in range(30)]]
        
        for num in arr:
            bits = [0 for _ in range(30)]
            for i in range(30):
                bits[i] += ((1 << i) & num) != 0
                bits[i] ^= prefix[-1][i]
            prefix.append(bits)
        
        ans = []
        for left,right in queries:
            total = 0
            for i in range(30):
                total += ((prefix[right+1][i]^prefix[left][i])<<i)
            ans.append(total)
        return ans