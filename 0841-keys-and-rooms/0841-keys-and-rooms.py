class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        count = 1
        visited = set()
        
        while(q):
            key = q.popleft()
            if key in visited:
                continue
            visited.add(key)
            for room in rooms[key]:
                q.append(room)
        return len(visited) == len(rooms)
            