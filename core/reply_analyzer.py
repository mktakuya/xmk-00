# -*- coding:utf-8 -*-
import re
from omikuji import Omikuji
from cputemp import CPUTemp
import settings

class ReplyAnalyzer:
    def __init__(self, bot, status):
        self.bot = bot
        self.status = status
        self.omikuji = Omikuji()
        self.cputemp = CPUTemp()

    def analyze_reply(self):
        self.text = self.status.text
        self.text = self.text.replace('@' + self.bot.botname + ' ', '')
        if settings.DEBUG is True: print self.text

        if re.match(u'おみくじ', self.text):
            if settings.DEBUG is True: print u'start omikuji...'
            self.bot.send_tweet(u'@' + self.status.author.screen_name + u' ' +
                    self.omikuji.choice_omikuji(), self.status.id)

        if re.match(u'cpu temp', self.text):
            if settings.DEBUG is True: print u'get cpu temp...'
            self.bot.send_tweet(u'@' + self.status.author.screen_name + u' ' +
                    self.cputemp.get_cpu_temp(), self.status.id)

