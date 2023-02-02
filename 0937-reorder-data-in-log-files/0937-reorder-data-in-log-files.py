class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digitsLogs = []
        letterLogs = []
        
        for log in logs:
            x = log.split(" ")
            if x[1].isdigit():
                digitsLogs.append(log)
            else:
                letterLogs.append(log)
                
        def compare(log1,log2):
            x = log1.split(" ")
            y = log2.split(" ")
            
            for i in range(1,min(len(x),len(y))):
                
                if x[i] < y[i]:
                    return -1
                elif y[i] < x[i]:
                    return 1
            return -1 if (len(x) < len(y) or x[0] <= y[0]) else 1
        
        letterLogs.sort(key= cmp_to_key(compare))
        letterLogs.extend(digitsLogs)
        
        return letterLogs
            
        