# -*- coding:utf-8 -*-
import socket

DEBUG = True
if socket.gethostname() == 'your host name': # デプロイ先のホスト名
    DEBUG = False

CONSUMER_KEY = 'your consumer_key'
CONSUMER_SECRET = 'your consumer_secret'
ACCESS_TOKEN = 'your access_token'
ACCESS_TOKEN_SECRET = 'your access_token_secret'

INTERVAL = 60   # DEBUGモード時のツイート間隔
if DEBUG is not True:
    INTERVAL = 420  # 本番モード時のツイート間隔

# http://www.drk7.jp/weather/ を参考に、XMLのURLとエリアを定義する。
WEATHER_XML_URL = 'http://www.drk7.jp/weather/xml/01.xml'
WEATHER_AREA = u'胆振地方'

KEY_WORDS = ''  # エゴサ用ワードを正規表現で

