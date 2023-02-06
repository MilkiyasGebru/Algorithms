class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0,1)])
        visited = set()
        
        shortest_path = 0
        while(q):
            size = len(q)
            for _ in range(size):
                
                position,speed = q.popleft()


                if position == target:
                    return shortest_path
                q.append((position + speed, speed * 2))

                if (position + speed  > target and speed > 0 ) or ( position + speed < target and speed < 0 ):
                    if speed < 0:
                        q.append((position , 1))
                    else:
                        q.append((position, -1))

            shortest_path += 1