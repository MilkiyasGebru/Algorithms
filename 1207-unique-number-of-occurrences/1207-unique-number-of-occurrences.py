class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        return max(Counter(Counter(arr).values()).values()) == 1