# Tweet up weather
import requests
import tweepy
from datetime import datetime
import time

consumer_key = '8AIPLClFD3zbxApToqkETb6EX'
consumer_secret = 'mkLhfWIdMzKCK5BcHfJ8HjxTb8hunbDUeMdPAgiUsvOaqybWAN'
access_token = '1279478070974582789-2XSABskD3A6QkpzfhxPr5B1ufsT5yO'
access_token_secret = 'YT2muFs0UFEkCTxBUT5ZCXtGiJJ0XOdntpXGjHLZYEAgR'

def twitter_auth():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	return tweepy.API(auth)

#------------------------------------------------------------------
city = 'Sofia'
url_hourly = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=d57422ef57a22fe4cceeea5524e9203c'

def get_weather():
	city_weather_hourly = requests.get(url_hourly.format(city)).json()

	rain_check = []
	for i in range(6):
		for x in city_weather_hourly['list'][i]['weather'][0]['description'].split():
			rain_check.append(x)

	forecast = False
	if 'rain' in rain_check:
		forecast = True

	return forecast
#------------------------------------------------------------------
def tweet_forecast():
	current_time_date = datetime.now().strftime("%d-%m-%Y")
	if get_weather():
		message = 'Take an umbrella, it might rain today!  ({})'.format(current_time_date)
	else:
		message = 'No worries today!  ({})'.format(current_time_date)
	return message

while True:
	current_time_hour = datetime.now().strftime("%H:%M:%S")
	if current_time_hour[:2] == '07':
		api = twitter_auth()
		api.update_status(tweet_forecast())
		print (tweet_forecast())
		time.sleep(86400)
	else:
		time.sleep(3600)