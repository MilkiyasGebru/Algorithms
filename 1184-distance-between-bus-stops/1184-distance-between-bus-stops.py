class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        total_distance = sum(distance)
        dis = 0
        while start != destination:
            dis += distance[start]
            start = (start + 1)%(len(distance))
        
        return min(dis,total_distance-dis)