class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        answer = [-1 for _ in range(len(nums))]
        for i in range(len(nums)-1,-1,-1):
            
            if q and q[0] - nums[i] != 1:
                q = deque([])
            q.appendleft(nums[i])
            if len(q) > k:
                q.pop()
            if len(q) < k:
                answer[i] = -1
            else:
                answer[i] = q[-1]
        while len(answer) > len(nums) -k + 1:
            answer.pop()
        return answer
            