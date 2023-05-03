class Solution:
    def isNumber(self, s: str) -> bool:
        
        def isInteger(s):
            
            if s in {"", "+", "-" }:
                return False
            
            boolean = s[0].isdigit() or s[0] in {"+","-"}
            
            for i in range(1,len(s)):
                boolean = boolean and s[i].isdigit()
            
            return boolean
        def isDecimal(s):
            
            if s in {"" ,"."}:
                return False
            
            arr = s.split(".")
            if len(arr) > 2:
                return False
            
            valid = arr[0] in {"+","-",""} and len(arr) > 1 and arr[1].isdecimal()
            return valid or (isInteger(arr[0])) and  ((len(arr)<=1) or isInteger(arr[1]) or arr[1] in {""})
            
        arr1 = s.split("e")
        arr2 = s.split("E")
        
        valid1 = len(arr1) < 3 and ((isInteger(arr1[0]) or isDecimal(arr1[0]))) and ((len(arr1)) < 2 or isInteger(arr1[1]) )
        valid2 = len(arr2) < 3 and ((isInteger(arr2[0]) or isDecimal(arr2[0]))) and ((len(arr2)) < 2 or isInteger(arr2[1]) )
        return valid1 or valid2
