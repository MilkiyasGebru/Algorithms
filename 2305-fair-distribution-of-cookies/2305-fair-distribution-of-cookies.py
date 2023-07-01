class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.maxx = math.inf
        cookies.sort(reverse=True)
        def backTrack(index,arr):
            
            if index == len(cookies):
                self.maxx = min(self.maxx,max(arr))
                return 
            
            for i in range(len(arr)):
                if arr[i] + cookies[index] < self.maxx:
                    arr[i] += cookies[index]
                    backTrack(index+1,arr)
                    arr[i] -= cookies[index]
        backTrack(0,[0 for _ in range(k)])
        return self.maxx
            