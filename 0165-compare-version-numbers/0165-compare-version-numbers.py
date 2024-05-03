class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = version1.split(".")
        version2 = version2.split(".")
        length = max(len(version1),len(version2))
        version1.extend([0 for _ in range(length-len(version1))])
        version2.extend([0 for _ in range(length-len(version2))])
        
        for i in range(length):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version2[i]) > int(version1[i]):
                return -1
        
        return 0