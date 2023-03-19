class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        def binary_search(left: int, right: int, fn: callable) -> int:
            while left < right:
                mid = left + right >> 1
                left, right = (mid + 1, right) if fn(mid) else (left, mid)
            return left

        def condition(limit: int) -> bool:

            def dfs(i: int) -> bool:
                if i == len(cookies):
                    return True
                for j in range(k):
                    if bags[j] + cookies[i] <= limit:
                        bags[j] += cookies[i]
                        if dfs(i + 1):
                            return True
                        bags[j] -= cookies[i]
                return False

            bags = [0] * k
            return not dfs(0)

        return binary_search(max(cookies), sum(cookies), condition)