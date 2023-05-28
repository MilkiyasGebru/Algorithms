class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        minn = [ arr[-1] for _ in range(len(arr)) ]
        for i in range(len(arr)-2,-1,-1):
            minn[i]=(min(arr[i],minn[i+1]))
        
        ans = 1
        maxx= arr[0]
        for i in range(len(arr)-1):
            maxx = max(arr[i],maxx)
            if maxx <= minn[i+1]:
                ans += 1
        
        return ans
        