class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)):
            a = 0
            for j in range(i,len(arr)):
                a ^= arr[j]
                b = 0
                for k in range(j+1,len(arr)):
                    b ^= arr[k]
                    count += 1 if a == b else 0
        return count