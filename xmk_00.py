#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import with_statement
import daemon
import tweepy
import multiprocessing
import datetime
import time
from core import settings
from core.botcore import BotCore
from core.tllistener import TLListener
from core.tweet_generator import TweetGenerator

def daily(bot):
    while True:
        time.sleep(settings.INTERVAL)
        tweet_generator = TweetGenerator()
        tweet = tweet_generator.generate_daily_tweet()
        bot.send_tweet(tweet)

def weather(bot):
    now = datetime.datetime.today()
    if (now.hour is 7) or (now.hour is 8):
        tweet_generator = TweetGenerator()
        tweet = tweet_generator.generate_weather_tweet()
        bot.send_tweet(tweet)

if __name__ == '__main__':
    if settings.DEBUG is not True:
        dc = daemon.DaemonContext()
        with dc:
            auth = tweepy.OAuthHandler(settings.CONSUMER_KEY,
                    settings.CONSUMER_SECRET)
            auth.set_access_token(settings.ACCESS_TOKEN,
                    settings.ACCESS_TOKEN_SECRET) 
            bot = BotCore(auth)
            bot.send_tweet(bot.botname + u' is started...')
            bot.follow_back()
            weather(bot)
            daily = multiprocessing.Process(target = daily, args=(bot,))
            daily.start()
            stream = tweepy.Stream(auth, TLListener(bot), secure=True)
            stream.userstream()
    else:
        auth = tweepy.OAuthHandler(settings.CONSUMER_KEY,
                settings.CONSUMER_SECRET)
        auth.set_access_token(settings.ACCESS_TOKEN,
                settings.ACCESS_TOKEN_SECRET) 
        bot = BotCore(auth)
        bot.send_tweet(bot.botname + u' is started...')
        #weather(bot) DEBUG == Trueの時は天気予報しない
        try:
            daily = multiprocessing.Process(target = daily, args=(bot,))
            daily.start()
            stream = tweepy.Stream(auth, TLListener(bot), secure=True)
            stream.userstream()
        except KeyboardInterrupt:
            bot.send_tweet(bot.botname + 
                    u' is going down for Keyboard Interrupt in 5 seconds!')
            time.sleep(5)
            bot.send_tweet(u'Bye.')

