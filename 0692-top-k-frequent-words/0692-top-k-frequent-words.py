import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        answer=[]
        heap=[]
        frequency ={}
        for i in words:
            if i not in frequency:
                frequency[i] =1
            else:
                frequency[i]+=1
        for f in frequency:
            heapq.heappush(heap,[-frequency[f],f])    
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer    