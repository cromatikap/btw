import unittest
from sample.User import User

class TestUser(unittest.TestCase):

  def test_check_config(self):
    user = User(['btw', 'list', 'files'])
    self.assertIs(user.check_config(), True)

  def test_get_input(self):
    user = User(['btw', 'list', 'files'])
    self.assertTrue(user.get_input(), "btw list files")

  def test_get_input_empty(self):
    user = User([])
    self.assertFalse(user.get_input())