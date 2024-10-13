class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        for i in range(len(times)):
            times[i].append(i)
        times.sort()
        free = []
        used = []
        room = 0
        for i in range(len(times)):
            arrival,leaving,index = times[i]
            while used and arrival >= used[0][0]:
                time,occupied_room = heapq.heappop(used)
                heapq.heappush(free,occupied_room)
            if len(free) == 0:
                heapq.heappush(free,room)
                room += 1
            free_room = heapq.heappop(free)
            if index == targetFriend:
                return free_room
            heapq.heappush(used,(leaving,free_room))