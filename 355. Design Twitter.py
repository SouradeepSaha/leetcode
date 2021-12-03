import heapq
from collections import deque


class Twitter:
    
    def checkCreateUser(self, userId) -> None:
        if userId not in self.twitter:
            self.twitter[userId] = {'following':set(), 'tweets': deque(maxlen=10)}

    def __init__(self):
        self.twitter = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.checkCreateUser(userId)
        self.twitter[userId]['tweets'].appendleft((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.twitter:
            return []
        
        h = [tweet for tweet in self.twitter[userId]['tweets']]
        heapify(h)
        for following in self.twitter[userId]['following']:
            for i in range(len(self.twitter[following]['tweets']) - 1, -1, -1):
                tweet = self.twitter[following]['tweets'][i]
                if len(h) < 10:
                    heappush(h, tweet)
                else:
                    if h[0][0] < tweet[0]:
                        heappushpop(h, tweet)
                    else:
                        break
        return [heappop(h)[1] for i in range(len(h))][::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.checkCreateUser(followerId)
        self.checkCreateUser(followeeId)
        self.twitter[followerId]['following'].add(followeeId)
    #print(self.twitter[followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.twitter[followerId]['following']:
            self.twitter[followerId]['following'].remove(followeeId)

