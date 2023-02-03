# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        f = defaultdict(list)
        def dfs(node,row,col):
            if not node:
                return 
            heapq.heappush(f[col],(row,node.val))
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
        dfs(root,0,0)
        answer=[]
        for key in sorted(f.keys()):
            l=[]
            while(f[key]):
                x,y=heapq.heappop(f[key])
                l.append(y)
            answer.append(l)
        return answer