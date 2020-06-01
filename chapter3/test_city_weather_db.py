import unittest

from chapter3.city_weather import HeFeng
from chapter3.city_weather_db import HefengDb

class TestCityweatherDbCase(unittest.TestCase):

      def test_save(self):
          hefengDb = HefengDb()
          hefengDb.save({"name":"wanguezheng","class":"19049"})
          hefengDb.show_all()
          results=hefengDb.find({"name":"wangyezheng"})
          for each in results:
              self.assertEqual("wangyezheng",each['name'])
              self.assertEqual("19049", each['class'])
          hefengDb.delete()
                #print(each)
          # self.asserEqual(4,hefeng.find_all())




      def test_save_all(self):
          hefeng=HeFeng()
          weathers=hefeng.get_all_weather(7)
          hefengDb=HefengDb()
          HefengDb.save_all(weathers)
          print("show_all")
          hefengDb.show_all()
          self.assertEqual(7,hefengDb.count())
          hefengDb.delete()


if __name__ == '__mian__':
    unittest.mian()
