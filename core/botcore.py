# -*- coding:utf-8 -*-
import tweepy
import time
import settings

class BotCore:
    def __init__(self, auth):
        self.auth = auth
        self.api = tweepy.API(auth_handler = self.auth, api_root = '/1.1')
        self.botname = self.auth.get_username()

    def send_tweet(self, tweet, in_reply_to = None):
        try:
            if settings.DEBUG is True: print u'sending tweet...\n', tweet
            self.api.update_status(tweet, in_reply_to_status_id = in_reply_to)
        except tweepy.error.TweepError as e:
            if settings.DEBUG is True: print u'tweet error.\n----------', str(e)

    def fav(self, status):
        if status.favorited is not True:
            if status.author is not self.botname:
                time.sleep(3)
                if settings.DEBUG is True: print u'fav this tweet.'
                try:
                    self.api.create_favorite(status.id)
                except:
                    pass

    def follow_back(self):
        follower = self.api.followers_ids(self.botname)
        friends = self.api.friends_ids(self.botname)

        set_apr = set(follower) - set(friends)
        list_apr = list(set_apr)

        for user in list_apr:
            self.api.create_friendship(user)

