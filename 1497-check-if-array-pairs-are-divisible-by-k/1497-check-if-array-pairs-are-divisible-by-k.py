class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr.sort(key=lambda x : x%k)
        left = 0
        while left < len(arr):
            if arr[left]%k != 0:
                break
            left += 1

        size = (len(arr) - left) 
        if size % 2 != 0:
            return False
        left,right = left,len(arr)-1
        while left < right:
            if (arr[left] + arr[right])%k != 0:
                return False
            
            left += 1
            right -= 1
        return True