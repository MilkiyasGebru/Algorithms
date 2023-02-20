
class Solution:
    def isIPv4(self,ip):
        parts = ip.split(".")
        return len(parts) == 4 and all(part in set(map(str, range(256))) for part in parts)
    def isIPv6(self,ip):
        parts = ip.split(":")
        hexdigits = '0123456789abcdef'
        return len(parts) == 8 and all(0 < len(part) <= 4 and all(c.lower() in hexdigits for c in part) for part in parts)
    def validIPAddress(self, queryIP: str) -> str:
        
        
        if self.isIPv4(queryIP): 
            return "IPv4"
        if self.isIPv6(queryIP):
            return "IPv6"
        return "Neither"