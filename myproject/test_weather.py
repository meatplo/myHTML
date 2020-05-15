import unittest

from city_weather import HeFeng

from city_weather_db import HefengDb


class TestCase(unittest.TestCase):

    def test_save(self):
        hefengDb = HefengDb()
        hefengDb.save({"name": "zhangbeirui", "class": "net19049"})
        hefengDb.show_all()
        results = hefengDb.find({"name": "zhangbeirui"})
        for each in results:
            self.assertEqual("zhangbeirui", each['name'])
            self.assertEqual("net19049", each['class'])
        hefengDb.delete()

    def test_save_all(self):
        hefeng = HeFeng()
        # codes = hefeng.get_city_code()
        # for each in codes:
        #   print(next(codes))
        each = hefeng.get_weather("CN101010200")
        print(each)
        hefengDb = HefengDb()
        hefengDb.save(each)


if __name__ == '__main__':
    unittest.main()
