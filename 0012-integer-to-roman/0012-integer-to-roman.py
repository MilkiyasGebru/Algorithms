class Solution:
    def intToRoman(self, num: int) -> str:
        
        roman_letter= { "M": 1000, "CM":900, "D" : 500, "CD" : 400, "C" : 100, "XC": 90, "L" : 50,"XL": 40, "X" : 10,"IX" : 9, "V" : 5, "IV" : 4, "I" : 1 }
        answer = []
        
        for roman in roman_letter.keys():
            
            for _ in range(num//roman_letter[roman]):
                answer.append(roman)
                
            num %= roman_letter[roman]
            
        return "".join(answer)
            