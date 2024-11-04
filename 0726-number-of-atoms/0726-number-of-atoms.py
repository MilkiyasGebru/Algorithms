class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        formula = formula[::-1]
        stack = [[1,defaultdict(int)]]
        i = 0
        element = num = ""
        while i < len(formula):
            if formula[i].islower():
                element += formula[i]
            elif formula[i].isupper():
                element += formula[i]
                element = element[::-1]
                if num == "":
                    num = "0"
                stack[-1][-1][element] += max(int(num[::-1]),1)
                element=""
                num = ""
            elif formula[i] == ")":
                if num == "":
                    num = "1"
                stack.append([int(num[::-1]), defaultdict(int)])
                num = ""
            elif formula[i].isdigit():
                num +=  formula[i]
            else:
                another_num,freq = stack.pop()
                for key in freq.keys():
                    freq[key] *= another_num
                    stack[-1][-1][key] += freq[key]
            i += 1
        answer = []
        for key in sorted(stack[-1][-1].keys()):
            answer.append(key)
            if stack[-1][-1][key] > 1:
                answer.append(str(stack[-1][-1][key]))
        return "".join(answer)
                 