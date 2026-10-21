class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetmap = defaultdict(list) # userId -> list of [-time, tweetIds]
        self.followmap = defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        # newest tweet has the smallest time so that it can be popped out first
        self.tweetmap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []    # ordered starting from recent
        minHeap = []

        self.followmap[userId].add(userId)

        for followeeId in self.followmap[userId]:
            if followeeId in self.tweetmap:
                index = len(self.tweetmap[followeeId]) - 1
                time, tweetId = self.tweetmap[followeeId][index]
                minHeap.append([time, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)