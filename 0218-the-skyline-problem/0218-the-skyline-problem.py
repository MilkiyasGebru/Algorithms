class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        f = defaultdict(int)
        remove = defaultdict(list)
        add = defaultdict(list)
        answer = []
        points = []
        heap = []
        for x,y,height in buildings:
            heapq.heappush(points,x)
            heapq.heappush(points,y)
            add[x].append(height)
            remove[y].append(height)
        prev,prevHeight = -math.inf,0
        
        while points:
            point = heapq.heappop(points)
            if point == prev:
                continue
            prev = point
            for height in add[point]:
                heapq.heappush(heap,-height)
            for height in remove[point]:
                f[height] += 1
            
            while heap and f[-heap[0]] > 0:
                height = heapq.heappop(heap)
                f[-1*height] -= 1
            height = 0 if len(heap) == 0 else -1*heap[0]
            if height != prevHeight:
                answer.append([point,height])
            prevHeight = height
        return answer
            