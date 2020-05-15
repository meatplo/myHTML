import pymongo


class HefengDb():
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.book_weather = self.client['weather']
        self.sheet_weather = self.book_weather['sheet_weather_3']

    def save(self, data):
        self.sheet_weather.insert_one(data)

    def show_all(self):
        all = self.sheet_weather.find()
        for each in all:
            print(each)

    def find(self, condition):
        return self.sheet_weather.find(condition)

    def delete(self):
        self.sheet_weather.delete_many({})


if __name__ == "__main__":
    hefengDb = HefengDb()
    hefengDb.save({"name": "zhangbeirui", "class": "net19049"})
    hefengDb.show_all()