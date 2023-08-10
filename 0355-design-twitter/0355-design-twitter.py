class Twitter:

    def __init__(self):
        self.user = defaultdict(set)
        self.tweet = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.time, tweetId])
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        self.user[userId].add(userId)
        for follower in self.user[userId]:
            if follower in self.tweet:
                index = len(self.tweet[follower]) - 1
                time, tweetId = self.tweet[follower][index]
                min_heap.append([time, tweetId, follower, index - 1])
        heapq.heapify(min_heap)

        while min_heap and len(res) < 10:
            time, tweetId, follower, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweet[follower][index]
                heapq.heappush(min_heap, [time, tweetId, follower, index - 1])
        
        return res
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.user[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user[followerId]:
            self.user[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)