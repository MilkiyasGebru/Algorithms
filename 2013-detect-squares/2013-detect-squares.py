class DetectSquares:

    def __init__(self):
        
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        
        self.points[(point[0],point[1])] += 1

    def count(self, point: List[int]) -> int:
        answer = 0
        keys = list(self.points.keys())
        for key in keys:
            if key[0] == point[0] and key[1] == point[1]:
                continue
            if key[0] == point[0]:
                
                diff = abs(key[1] - point[1])
                
                answer += self.points[key] * (self.points[(key[0] + diff, key[1])] * self.points[(point[0] + diff, point[1])] + self.points[(key[0] - diff, key[1])] * self.points[(point[0] - diff, point[1])])
            
        return answer
    
    
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)