class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        
        left = deque([])
        answer = []
        array = []
        for i in range(len(positions)):
            array.append([positions[i],healths[i],directions[i],i])
        array.sort(key=lambda x : x[0])
        for i in range(len(array)-1,-1,-1):
            
            if array[i][2] == "R":
                
                while left and left[0][0] < array[i][1]:
                    
                    left.popleft()
                    array[i][1] -= 1
                
                if left and left[0][0] == array[i][1]:
                    left.popleft()
                elif left and left[0][0] > array[i][1]:
                    left[0][0] -= 1
                elif not left and array[i][1] > 0:
                    answer.append([array[i][1],array[i][-1]])
            else:
                left.appendleft([array[i][1],array[i][-1]])
        
        answer.extend(left)
        answer.sort(key = lambda x : x[-1])
        return [answer[i][0] for i in range(len(answer))]