# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        self.levels = defaultdict(lambda : [-1,-1])
        self.f = {}
        
        def traverse(node,level):
            
            if not node:
                return -1
            
            max_= max(1 + traverse(node.left,level+1),1 + traverse(node.right,level+1))
            self.f[node.val] = level,max_
            
            if max_ > self.levels[level][0]:
                
                self.levels[level][1] = self.levels[level][0]
                self.levels[level][0] = max_
                
            else:
                self.levels[level][1] = max(max_,self.levels[level][1])
                
            return max_
        traverse(root,0)
        
        answer = []
        
        for query in queries:
            
            level,height = self.f[query]
            
            if height == self.levels[level][0]:
                answer.append(self.levels[level][1]+level)
                
            else:
                answer.append(self.levels[level][0] + level)
                
        return answer
            
            
            
                 