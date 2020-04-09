import unittest
from unittest import mock

from post_youdao import *

class PostYoudaoTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)

    def test_grt_ts(self):
        #import time
        #t=time.time()
        #ts=str(int(round(ts*1000)))
        #print(ts)
        get_ts=mock.Mock(return_value='1586438056396')
        self.assertEqual('1586438056396',get_ts())

    def test_get_salt(self):
        self.assertEqual('15864380563960',get_salt())


if __name__ == '__main__':
    unittest.main()
