class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        array =[-float("inf")]
        for num in nums:
            
            if num > array[-1]:
                array.append(num)
            else:
                for i in range(len(array)):
                    if num <= array[i]:
                        array[i] = num
                        break
            
        return len(array) > 3