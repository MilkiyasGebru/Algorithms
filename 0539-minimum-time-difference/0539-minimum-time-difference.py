class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            hour,minute = map(int,time.split(":"))
            minutes.append(hour*60 + minute)
        minutes.sort()
        total_minutes = 24*60
        ans = min(minutes[-1]-minutes[0],total_minutes - (minutes[-1]-minutes[0]))
        for i in range(1,len(minutes)):
            ans = min(ans,minutes[i]-minutes[i-1],total_minutes - (minutes[i]-minutes[i-1]))
        return ans