class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""
        for i in range(len(strs[0])):
            
            for string in strs:
                
                if len(string)==i or string[i]!=strs[0][i]:
                    return result
            result += strs[0][i]
            
        return result    