# -*- coding:utf-8 -*-
import commands

class CPUTemp:
    def __init__(self):
        pass

    def get_cpu_temp(self):
        return commands.getoutput('vcgencmd measure_temp')

