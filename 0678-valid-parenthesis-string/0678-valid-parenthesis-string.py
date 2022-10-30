class Solution:
    def checkValidString(self, s: str) -> bool:
        @lru_cache(None)
        def dp(index,count):
            
            if index == len(s):
                return count == 0
            if count < 0:
                return False
            if s[index]=="(":
                return dp(index+1,count+1)
            elif s[index] == ")":
                return dp(index+1,count-1)
            else:
                return dp(index+1,count+1) or dp(index+1,count-1) or dp(index+1,count)
        return dp(0,0)