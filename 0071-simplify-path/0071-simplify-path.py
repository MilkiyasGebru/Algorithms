class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split('/')
        stack = []
        
        for file in path:
            
            if file == "" or file == "." :
                continue
                
            elif  file == "..":
                
                if stack:
                    stack.pop()
                    
            else:
                stack.append(file)
                
        return "/" + '/'.join(stack)