''' Scrapping the Weather Forecast Details from the https://weather.com '''

import sys
import requests
from bs4 import BeautifulSoup

def weather_forecast_details(city):
    ''' To get the weather forecast details for a particular city '''
    try:
        weather = {}

        response = requests.get(
            'https://api.weather.com/v3/location/search?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&language=en-IN&locationType=locale&query=' + city)  # pylint: disable=line-too-long
        response_data = response.json()

        placeid = response_data.get('location').get('placeId')[0]

        page_content = requests.get('https://weather.com/en-IN/weather/today/l/' + placeid)

        soup = BeautifulSoup(page_content.content, "html.parser")

        weather["loc"] = soup.find("header", {"class": "loc-container"}).text
        weather["temp"] = soup.find("div", {"class": "today_nowcard-temp"}).text
        weather["phrase"] = soup.find("div", {"class": "today_nowcard-phrase"}).text
        weather["deg"] = soup.find("div", {"class": "today_nowcard-feels"}).text

        print(weather)

    except:                                            # pylint:disable=bare-except
        print("No City Found!")


if __name__ == '__main__':
    weather_forecast_details(sys.argv[1])
