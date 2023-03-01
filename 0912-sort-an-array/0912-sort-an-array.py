class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left,right):
            if left == right:
                return [nums[right]]
            else:
                A,B=merge(left,(left+right)//2) , merge((left+right)//2+1,right)
                arr=[]
                i,j=0,0
                while(i < len(A) and j < len(B)):
                    if A[i] > B[j]:
                        arr.append(B[j])
                        j+=1
                    else:
                        arr.append(A[i])
                        i+=1
                while(i < len(A)):
                    arr.append(A[i])
                    i+=1
                while(j < len(B)):
                    arr.append(B[j])
                    j+=1
                    
                return arr
        return merge(0,len(nums)-1)    
            
                