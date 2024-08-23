class Solution:
    def fractionAddition(self, expression: str) -> str:
        divisors = [2,3,5,7]
        numo = []
        deno = []
        if expression[0] != "-":
            expression = "+"+expression
        i = 0
        while i < len(expression):
            
            j = i + 1
            numerator = denominator = 0
            while j < len(expression) and expression[j].isdigit():
                numerator *= 10
                numerator += int(expression[j])
                j += 1
            numo.append(numerator if expression[i] == "+" else -numerator )
            j += 1
            while j < len(expression) and expression[j].isdigit():
                denominator *= 10
                denominator += int(expression[j])
                j += 1
            deno.append(denominator)
            i = j
        total_product = 1
        fraction = 0
        for num in deno:
            total_product *= num
        for i in range(len(deno)):
            fraction += (numo[i]*total_product)//deno[i]
        for i in range(len(divisors)):
            while fraction%divisors[i] == 0 and total_product%divisors[i] == 0:
                fraction //= divisors[i]
                total_product //= divisors[i]
        return str(fraction)+"/"+str(total_product)
        
            