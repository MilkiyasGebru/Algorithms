class Solution:
    
    def evaluate_expression(self,s,f):
        numbers = []
        operators = []
        prev_num = 0
        for c in s:
            if c in ["+","-"]:
                numbers.append(prev_num)
                prev_num = 0
                operators.append(c)
            else:
                prev_num = prev_num*10 + int(c)
        numbers.append(prev_num)
        
        operators.reverse()
        numbers.reverse()
        
        while operators:
            operator = operators.pop()
            num1 = numbers.pop()
            num2 = numbers.pop()
            numbers.append(f[operator](num1,num2))
        return numbers.pop()
        
    def calculate(self, s: str) -> int:
        
        s = "(" + s + ")"
        stack = [[]]
        f = {
            "+" : lambda a,b : a + b,
            "-" : lambda a,b : a - b
        }
        for c in s:
            if c == " ":
                continue
            if c == "(":
                stack.append([])
            elif c == ")":
                num = self.evaluate_expression(stack[-1],f)
                stack.pop()
                stack[-1].append(str(num))
            else:
                stack[-1].append(c)
        return int(stack[-1][0])