class Solution:
    def calc(self,word1,word2):
        diff = 0
        for i in range(8):
            if word1[i]!=word2[i]:
                diff +=1
        return diff == 1
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        queue = deque()
        visited = set()
        queue.append(start)
        
        mutation = 0
        while(queue):
            x = len(queue)
            for _ in range(x):
                gene = queue.popleft()
                if gene in visited:
                    continue
                visited.add(gene)
                if gene == end:
                    return mutation
                for element in bank:
                    if element not in visited and self.calc(element,gene):
                        queue.append(element)
            mutation += 1
        return -1
        