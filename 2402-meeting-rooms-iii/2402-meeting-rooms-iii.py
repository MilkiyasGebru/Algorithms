class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        
        heap = []
        rooms = []
        
        for i in range(n):
            heappush(rooms,i)
        
        f =defaultdict(int)
        
        meetings.sort()
        
        for start,end in meetings:
            
            while heap and heap[0][0] <= start:
                
                x,room = heappop(heap)
                heappush(rooms,room)
                
            if len(heap) == n:
                
                x,room = heappop(heap)
                heappush(heap,(end-start + x,room))
            else:
                
                room = heappop(rooms)
                heappush(heap,(end,room))
            f[room] += 1
            
        max_ = room = 0
        for i in range(n):
            if f[i] > max_:
                max_ = f[i]
                room = i
        
        return room
                
            
            
                
            