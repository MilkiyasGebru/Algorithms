class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        nums.append(0)
        f = defaultdict(lambda : deque())
        total = left =  0
        for right in range(len(nums)):
            if nums[right] == maxK:
                f[maxK].append(right)
            if nums[right] == minK:
                f[minK].append(right)
            
            if nums[right] > maxK or nums[right] < minK:
                
                while left <= right:
                    minIndex = f[minK][0] if f[minK] else -1
                    maxIndex = f[maxK][0] if f[maxK] else -1
                    
                    if f[minK] and nums[f[minK][0]] == nums[left]:
                        f[minK].popleft()
                    if f[maxK] and nums[f[maxK][0]] == nums[left]:
                        f[maxK].popleft()
                    if minIndex != -1 and maxIndex != -1:
                        total += right - max(minIndex,maxIndex)
                    left += 1
                f = defaultdict(lambda:deque())
        
        return total
        
        
            # ,5,2,1,5,7,5
            # 1,3,5,2,1,2,3,6
            