class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        items.sort()
        for i in range(len(queries)):
            queries[i] = [queries[i],i]
        queries.sort()
        answer = [0 for _ in range(len(queries))]
        max_beauty = 0
        j = 0
        for i in range(len(queries)):
            while j < len(items) and items[j][0] <= queries[i][0]:
                max_beauty = max(max_beauty, items[j][1])
                j += 1
            answer[queries[i][1]] = max_beauty
        return answer