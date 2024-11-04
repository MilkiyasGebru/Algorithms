class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = [[1, ""]]
        num = i = 0
        
        while i < len(s):
            
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == "[":
                stack.append([num,""])
                num = 0
            elif s[i] != "]":
                stack[-1][-1] += s[i]
            else:
                val,string = stack.pop()
                stack[-1][-1] += val*string
            i += 1
        return stack[-1][-1]
                
            