class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        # if its closing sign return
        stack = []
        f = {
            "!": lambda a,b : not a,
            "|": lambda a,b : a or b,
            "&": lambda a,b : a and b
        }
        for i in range(len(expression)):
            if expression[i] in {"|","&","!"}:
                stack.append([expression[i]])
                
            elif expression[i] in "(,":
                continue
            
            elif expression[i] in "tf":
                if stack[-1][0] == "!":
                    stack[-1].append(not (expression[i] == "t"))
                elif len(stack[-1]) == 1:
                    stack[-1].append(expression[i]=="t")
                else:
                    stack[-1][-1] = f[stack[-1][0]](stack[-1][-1],expression[i]=="t")
            else:
                _,value = stack.pop()
                if len(stack) == 0:
                    return value
                if stack[-1][0] == "!":
                    stack[-1].append(not(value))
                elif len(stack[-1]) == 1:
                    stack[-1].append(value)
                else:
                    stack[-1][-1] = f[stack[-1][0]](stack[-1][-1],value)
                        
        print(stack)