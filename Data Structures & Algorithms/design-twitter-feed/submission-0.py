import heapq

class Twitter:

    def __init__(self): 
        self.time = 0
        self.user_follower_map = defaultdict(set)
        self.user_tweet_map = defaultdict(list) 

    # time - O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweet_map[userId].append((self.time, tweetId))
        self.time  -= 1

    # time - O(1)
    def getRecentTweetByUserId(self, user_id):
        index = len(self.user_tweet_map[user_id]) - 1
        time, tweetId = self.user_tweet_map[user_id][index]
        return (time, tweetId, user_id, index-1)

    # time - O(k + 10 log k)
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        # tweets of user's followees
        for followeeId in self.user_follower_map[userId]:
            if followeeId not in self.user_tweet_map: continue
            tweet_details = self.getRecentTweetByUserId(followeeId)
            min_heap.append(tweet_details)

        # tweets of user
        if userId in self.user_tweet_map:
            tweet_details = self.getRecentTweetByUserId(userId)
            min_heap.append(tweet_details)
        
        if (len(min_heap) == 0): return res
            
        heapq.heapify(min_heap)

        while min_heap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.user_tweet_map[followeeId][index]
                heapq.heappush(min_heap, (time, tweetId, followeeId, index-1))
        
        return res
        
    # time - O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId: return None
        self.user_follower_map[followerId].add(followeeId)

    # time - O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId: return None
        self.user_follower_map[followerId].discard(followeeId)
