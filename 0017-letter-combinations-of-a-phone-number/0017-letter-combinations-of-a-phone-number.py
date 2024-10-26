class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        d = {}
        d['2'] = ['a','b','c']
        d['3'] = ['d','e','f']
        d['4'] = ['g','h','i']
        d['5'] = ['j','k','l']
        d['6'] = ['m','n','o']
        d['7'] = ['p','q','r','s']
        d['8'] = ['t','u','v']
        d['9'] = ['w','x','y','z']
        if len(digits)==0:return []
        def rec(i):
            if i==len(digits):
                return [""]
            else:
                arr = rec(i+1)
                answer =[]
               
                for letter in d[digits[i]]:
                    for each in arr:
                        answer.append(letter+each)
                return answer 
        return rec(0)    