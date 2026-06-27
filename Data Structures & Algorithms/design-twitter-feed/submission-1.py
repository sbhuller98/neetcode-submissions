from collections import defaultdict
class Twitter:

    def __init__(self):
        self.followe = defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []

        followers = set()
        if userId in self.followe:
            followers = self.followe[userId]
        followers.add(userId)
        
        i = -1
        while self.tweets and len(ans) < 10 and i + len(self.tweets) >= 0:
            usr, tweet = self.tweets[i]
            if usr in followers:
                ans.append(tweet)
            i -= 1

        return ans
                  

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followe[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followe[followerId].discard(followeeId)
