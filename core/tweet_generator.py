# -*- coding:utf-8 -*-
import tweets
import random
import datetime
import settings
from weather_forecaster import WeatherForecaster

class TweetGenerator:
    def __init__(self):
        pass

    def generate_daily_tweet(self):
        reload(tweets)
        tweet_list = tweets.tweet_list
        return tweets.tweet_list[random.randint(0, len(tweet_list) - 1)]

    def generate_weather_tweet(self):
        weather_forecaster = WeatherForecaster()
        tweet = u"""おはようございます。
{today} の {area} の天気は、
{weather} です。
最高気温は {max_temperature}℃ で、最低気温は {min_temperature}℃ です。
今日も一日頑張りましょう。""".format(today = \
        str(datetime.date.today()).replace('-', '/'),area = settings.WEATHER_AREA,
        weather = weather_forecaster.get_today_weather(),
        max_temperature = weather_forecaster.get_today_max_temperature(),
        min_temperature = weather_forecaster.get_today_min_temperature()
        )
        return tweet

