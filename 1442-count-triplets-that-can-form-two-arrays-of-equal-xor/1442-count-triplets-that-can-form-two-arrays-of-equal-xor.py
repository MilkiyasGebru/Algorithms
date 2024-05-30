class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        a = 0
        for i in range(len(arr)):
            a ^= arr[i]
            b = 0
            for j in range(i+1,len(arr)):
                b ^= arr[j]
                count += prefix[a^b]
            prefix[a] += 1
        return count