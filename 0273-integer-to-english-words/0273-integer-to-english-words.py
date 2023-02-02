class Solution:
    def numberToWords(self, num: int) -> str:
        
        power={10**9:"Billion",10**6:"Million",10**3:"Thousand",10**2:"Hundred"}
        digits={90:"Ninety",80:"Eighty",70:"Seventy",60:"Sixty",50:"Fifty",40:"Forty",30:"Thirty",20:"Twenty",19 : "Nineteen",18:"Eighteen",17: "Seventeen",16 : "Sixteen",15:"Fifteen",14:"Fourteen",13:"Thirteen",12:"Twelve",11:"Eleven", 10:"Ten",9:"Nine",8:"Eight",7:"Seven",6:"Six",5:"Five",4:"Four",3:"Three",2:"Two",1:"One"}
        @lru_cache(None)
        def rec(num):
            if num==0:
                return ""
            for key,value in power.items():
                
                if num < 100:
                    break
                if num//key != 0:
                    if num%key==0:
                        return rec(num//key)+" "+value
                    return rec(num//key)+" "+value+" "+rec(num%key)
            for key,value in digits.items():
                if num//key != 0:
                    if num%key==0:
                        return digits[key]
                    return digits[key]+" "+rec(num%key)
                
        return rec(num) if rec(num)!="" else "Zero"        