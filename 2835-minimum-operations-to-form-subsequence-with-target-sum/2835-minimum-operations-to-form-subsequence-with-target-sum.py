class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        
        f = Counter(nums)
        array = []
        
        for i in range(31, -1, -1):
            if target >= 2 ** i:
                array.append(2 ** i)
                target -= 2 ** i
            
        array.reverse()
        count = 0
        less_num = 0
        for i in range(len(array)):
            
            for j in range(0,32):
                if (2**j) <= array[i] :
                    less_num += f[(2**j)]*(2**j)
                    f[(2**j)] = 0
                    
                elif f[(2**j)]:
                    break
            if array[i] > less_num:
                if j == 31:
                    return -1
                while 2**j != array[i]:
                    
                    f[(2**j)] -= 1
                    count += 1
                    j -= 1
                    f[(2**j)] += 2
                    
                f[(2**j)] -= 1
            else:
                less_num -= array[i]
                                
            
            
            
        
        return count
            
        
        