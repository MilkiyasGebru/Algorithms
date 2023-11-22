class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        f = defaultdict(list)
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                f[row+col].append(nums[row][col])
        
        answer = []
        for key in sorted(f.keys()):
            answer.extend(f[key][::-1])
        
        return answer