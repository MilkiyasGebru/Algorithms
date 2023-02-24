class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            intervals.append((left, right))

        intervals.sort(key=lambda x: x[0])
        curr_end = 0
        next_end = 0
        num_taps = 0
        i = 0

        while i <= n and curr_end < n:
            while i <= n and intervals[i][0] <= curr_end:
                next_end = max(next_end, intervals[i][1])
                i += 1

            if curr_end == next_end:
                return -1

            num_taps += 1
            curr_end = next_end

        return num_taps
