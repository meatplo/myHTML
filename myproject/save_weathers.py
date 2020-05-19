from city_weather import HeFeng
from city_weather_db import HefengDb

if __name__ == '__main__':
    hefeng = HeFeng()
    weathers = hefeng.get_all_weather(50)
    hefengDb = HefengDb()
    hefengDb.save_all(weathers)
    hefengDb.show_all()