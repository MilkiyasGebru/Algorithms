class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def countSubarray( count ):
            left = 0
            frequency = defaultdict(int)
            visited = set()
            total = 0
            
            for right in range(len(nums)):
                visited.add(nums[right])
                frequency[nums[right]] += 1
                
                while(len(visited) > count):
                    frequency[nums[left]] -= 1
                    if frequency[nums[left]] == 0:
                        visited.remove(nums[left])
                    
                    left += 1
                
                total += right - left + 1
            return total
        
        return countSubarray(k) - countSubarray(k-1)
            