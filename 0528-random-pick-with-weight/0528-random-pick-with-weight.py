class Solution:

    def __init__(self, w: List[int]):
        
        self.weightIndex = [w[0]]
        
        for i in range(1,len(w)):
            
            self.weightIndex.append(self.weightIndex[-1] + w[i])
            
        self.total = sum(w)
        
    def pickIndex(self) -> int:
        
        randomNum = random.randint(1,self.total)

        
        return self.binarySearch(randomNum)
    
    def binarySearch(self,val):
        
        left = 0
        right = len(self.weightIndex)-1
        index = 0
        
        while(left <= right):
            
            mid = (left + right)//2
            
            if self.weightIndex[mid]  > val:
                right = mid - 1
                
            elif self.weightIndex[mid] == val:
                return mid
            
            else:
                index = mid + 1
                left = mid + 1
                
        return index
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()