class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l = 0
        x=[]
        while(l<len(nums)):
            s=0
            for r in range(l,len(nums)):
                s+=nums[r]
                x.append(s)
            l+=1    
        x.sort()
        return (sum(x[left-1:right]))%(10**9+7)