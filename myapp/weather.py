import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather(city="Abuja, NG"):
    city = str(city)
    city = city.capitalize().strip()
    city = f'{city} State, NG' 
    
    request_url= f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}units=metric'
    
    #print(request_url)
    
    weather_data = requests.get(request_url).json()
    
    weather_data = pprint(weather_data)
    
    State = print(weather_data["name"])
    Temp = print(The temperature is {weather_data["main"]["temp"]})
    Feels = print({weather_data["main"]["feels_like"]})
    Weather = print({weather_data["weather"][0]["description"]})
    
    return weather_data
    


if __name__ == "__main__":
    
    print("\n******Current Weather Condition******")
    
    State = input('please enter a state name: ')
    State = State.capitalize().strip()
   
    city = f'{State} State, NG' 
    
    weather_data = get_current_weather(city)
    
    print('\n')
    pprint(weather_data)
        
    #State = f'\nCurrent weather for {weather_data['name']}'
    #Country = f'Country: {weather_data['sys']['country']}'
   # Temp = f'\nThe temperature is {weather_data['main']['temp']}'
   # Feels = f'\nThe weather feels like {weather_data['main']['feels_like']}'
   # Weather = f'The Sky {weather_data["weather"][0]["description"]}'
   # Wind = f'The wind degree is {weather_data['wind']['deg']}, gust is {weather_data['wind']['gust']}, speed is {weather_data['wind']['speed']}'
    
   # print(State)
   # print(Country)
   # print(Temp)
   # print(Feels)
   # print(Weather)
   # print(Wind)
    
    
    