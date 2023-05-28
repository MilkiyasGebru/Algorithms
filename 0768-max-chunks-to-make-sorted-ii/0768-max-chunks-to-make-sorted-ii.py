class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        sorted_arr = sorted(arr)
        left,count,length = 0,0,len(arr)
        for index in range(length):
            if sorted_arr[left:index+1] == sorted(arr[left:index+1]):
                count+=1
                left = index + 1
        return count
        