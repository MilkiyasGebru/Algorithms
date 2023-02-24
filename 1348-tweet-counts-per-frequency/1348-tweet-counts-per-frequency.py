class TweetCounts:

    def __init__(self):
        self.tweet_map = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweet_map[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        interval = {"minute": 60, "hour": 3600, "day": 86400}[freq]
        result = []
        tweets = self.tweet_map.get(tweetName, [])
        tweets.sort()
        i = startTime
        while i <= endTime:
            j = min(i + interval, endTime + 1)
            count = 0
            for tweet_time in tweets:
                if i <= tweet_time < j:
                    count += 1
                elif tweet_time >= j:
                    break
            result.append(count)
            i = j
            
        return result


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)