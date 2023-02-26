class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        op = {"+":operator.add}
        def perform(a,b,op):
            
            if op == "+":
                return [x+y for x in a for y in b]
            elif op == "-":
                return [x-y for x in a for y in b]
            return [x*y for x in a for y in b]
        
        @lru_cache(None)
        def calc(s):
            
            digit = ""
            if s.isnumeric():
                return [int(s)]
            index = 0
            ans = []
            while(index < len(s)):
                while(index < len(s) and s.isdigit() ):
                    digit += s[index]
                    index += 1
                if index == len(s):
                    continue
                ans1 = calc(s[0:index])
                ans2 = calc(s[index+1:])
                ans.extend(perform(ans1,ans2,s[index]))
                digit = ""
                index += 1
            return ans
        return calc(expression)
                
                
                
                
            
            
            
            