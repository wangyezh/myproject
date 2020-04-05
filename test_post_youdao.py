import unittest
from unittest import mock

from post_youdao import *

class PostYoudaoTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)

    def test_grt_ts(self):
        #import time
        #ts=time.time()
        #ts=str(int(round(ts*1000)))
        #print(ts)
        get_ts=mock.Mock(return_value='1585905747189')
        self.assertEqual('1585905747189',get_ts())


if __name__ == '__main__':
    unittest.main()
