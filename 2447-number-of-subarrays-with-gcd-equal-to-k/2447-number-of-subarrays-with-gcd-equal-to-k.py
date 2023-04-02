class Solution:
    def findGCD(self,num1,num2):
        if num2 == 0:
            return num1
        
        return self.findGCD(num2,num1%num2)
        
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        answer = 0
        
        for i in range(len(nums)):
            prev = nums[i]
            for j in range(i,len(nums)):
                prev = self.findGCD(max(nums[j],prev),min(nums[j],prev))
                if prev == k:
                    answer += 1
                elif prev < k:
                    break
        
        return answer
        
        