class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        answer = [0 for _ in range(len(people))]
        heap = []
        flowers.sort()
        new_peoples = []
        
        for i in range(len(people)):
            
            new_peoples.append((people[i],i))
            
        new_peoples.sort()
        i = 0
        
        for person,idx in new_peoples:
            
            while i < len(flowers) and flowers[i][0] <= person:
                heappush(heap,flowers[i][1])
                i += 1
                
            while heap and person > heap[0]:
                heappop(heap)
                
            answer[idx]+= len(heap)
        
        return answer
            