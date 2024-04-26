class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        sorted_nums = sorted(nums)
        another_arr = [deque([sorted_nums[0]])]
        for i in range(1,len(sorted_nums)):
            if another_arr[-1][-1] + limit >= sorted_nums[i]:
                another_arr[-1].append(sorted_nums[i])
            else:
                another_arr.append(deque([sorted_nums[i]]))
        
        
        f = defaultdict(int)
        for i in range(len(another_arr)):
            for num in another_arr[i]:
                f[num] = i
        answer = []
        for num in nums:
            answer.append(another_arr[f[num]].popleft())
        return answer