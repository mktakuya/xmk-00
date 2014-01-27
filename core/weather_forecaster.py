# -*- coding:utf-8 -*-
import urllib
import urllib2
import datetime
from BeautifulSoup import BeautifulStoneSoup
import settings

class WeatherForecaster:
    def __init__(self):
        url = settings.WEATHER_XML_URL
        response = urllib2.urlopen(url)
        soup = BeautifulStoneSoup(response)
        self.area = settings.WEATHER_AREA
        area_weather = soup.find('area', attrs={'id': self.area})
        self.today = area_weather.find('info',
                attrs = {'date': str(datetime.date.today()).replace('-', '/')})

    def get_today_weather(self):
        return unicode(self.today.weather.renderContents(), 'utf-8')

    def get_today_max_temperature(self):
        return unicode(self.today.find('range',
            attrs={'centigrade':'max'}).renderContents(), 'utf-8')

    def get_today_min_temperature(self):
        return unicode(self.today.find('range',
            attrs={'centigrade':'min'}).renderContents(), 'utf-8')

