class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        answer = ""
        string = ""
        for i in range(min(len(str1),len(str2))):
            if str1[i] != str2[i]:
                return answer
            string += str1[i]
            
            if (len(str1) // len(string))* string == str1 and (len(str2) // len(string))* string == str2:
                answer = string
        
        return answer
            