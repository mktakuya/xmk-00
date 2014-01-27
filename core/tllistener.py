# -*- coding:utf-8 -*-
from tweepy.streaming import StreamListener
from matcher import Matcher
from reply_analyzer import ReplyAnalyzer
import settings


class TLListener(StreamListener):
    def __init__(self, bot):
        StreamListener.__init__(self, api=None)
        self.bot = bot
        self.count = 0

    def on_status(self, status):
        try:
            matcher = Matcher(status.text)
            if status.text.find(u'@' + self.bot.botname) is not -1:
                self.bot.fav(status)
                reply_analyzer = ReplyAnalyzer(self.bot, status)
                reply_analyzer.analyze_reply()

        except AttributeError as e:
            pass

