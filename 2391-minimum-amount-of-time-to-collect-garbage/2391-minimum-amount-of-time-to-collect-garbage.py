class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        metal_bus = paper_bus = glass_bus = 0
        travel = [0] + travel
        for i in range(1,len(travel)):
            travel[i] += travel[i-1]
        total_time = 0
        for i in range(len(garbage)):
            
            if "G" in garbage[i]:
                total_time += garbage[i].count("G")
                total_time += travel[i] - travel[glass_bus]
                glass_bus = i
            if "M" in garbage[i]:
                total_time += garbage[i].count("M")
                total_time += travel[i] - travel[metal_bus]
                metal_bus = i
            if "P" in garbage[i]:
                total_time += garbage[i].count("P")
                total_time += travel[i] - travel[paper_bus]
                paper_bus = i
        
        return total_time
    
        