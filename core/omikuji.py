# -*- coding:utf-8 -*-
import random

omikuji_sticks = [
        u'大吉',
        u'中吉',
        u'小吉',
        u'吉',
        u'末吉',
        u'凶',
        u'大凶',
        u'マジキチ',
        ]

class Omikuji:
    def __init__(self):
        pass

    def choice_omikuji(self):
        return random.choice(omikuji_sticks)

