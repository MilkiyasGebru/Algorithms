class Solution:
    
    def binary_search(self,spell,potions,sucess):
        left = 0
        right = len(potions)
        
        while left < right:
            
            mid = (left + right)//2
            
            if spell*potions[mid] >= sucess:
                right = mid 
            else:
                left = mid + 1
        
        return len(potions) - left
        
    
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        pairs = []
        
        for spell in spells:
            pairs.append(self.binary_search(spell,potions,success))
        
        return pairs