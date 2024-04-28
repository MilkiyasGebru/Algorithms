class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        @cache
        def dp(curr_index,key_index):
            
            if key_index >= len(key):
                return 0
            
            if ring[curr_index] == key[key_index]:
                return 1 + dp(curr_index, key_index + 1)
            
            left_most = right_most = curr_index
            left_cost = right_cost = 0
            
            while ring[left_most] != key[key_index]:
                
                left_cost += 1
                left_most -= 1
                left_most %= len(ring)
                
            while ring[right_most] != key[key_index]:
                
                right_cost += 1
                right_most += 1
                right_most %= len(ring)
            
            return 1 + min(left_cost + dp(left_most,key_index+1),right_cost + dp(right_most,key_index+1))
        
        return dp(0,0)