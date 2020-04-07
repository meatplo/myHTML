import unittest
from unittest import mock

from post_youdao import *


class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_ts(self):
        get_ts = mock.Mock(return_value='1584684147229')
        self.assertEqual('1584684147229', get_ts())

    def test_get_salt(self):
        get_salt=mock.Mock(return_value="15846841472292")
        self.assertEqual('15846841472292', get_salt())

    def test_get_sign(self):
        self.assertEqual('2a57c66e7e063f81f8b730a87a41514b',get_sign())


if __name__ == '__main__':
    unittest.main()
