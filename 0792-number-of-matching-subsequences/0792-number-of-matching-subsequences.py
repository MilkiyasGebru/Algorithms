class Solution:
    def binary_search(self,arr,index):
        left,right = 0,len(arr)
        
        while left < right:
            
            mid = (left + right)//2
            
            if arr[mid] >= index:
                right = mid
            else:
                left = mid + 1
        
        return arr[left] if 0 <= left < len(arr) and arr[left] >= index else -1 
        
        
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        
        char_indexs = defaultdict(list)
        for i in range(len(s)):
            
            char_indexs[s[i]].append(i)
        prev_i = 0
        for character in "bb":
            prev_i = self.binary_search(char_indexs[character],prev_i)
        
        matchingSub = 0
        for i in range(len(words)):
            prev_i,isValid = 0,True
            for j in range(len(words[i])):
                prev_i = self.binary_search(char_indexs[words[i][j]],prev_i)
                isValid = isValid and (prev_i != -1)
                prev_i += 1
            matchingSub += isValid
        
        return matchingSub
        
        
        
        