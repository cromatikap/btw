import unittest
from sample.User import User

class TestUser(unittest.TestCase):

  # user.init()

  def test_init_true(self):
    user = User(['btw', 'list', 'files'], 'tests/.btw-history-good-format')
    self.assertIs(user.init(), True)
  
  def test_init_false(self):
    user = User([], 'tests/.btw-history-wrong-format')
    self.assertIs(user.init(), False)
  
  def test_init_history_error(self):
    user = User(['btw', 'list', 'files'], 'tests/.btw-history-wrong-format')
    expected_error = 'tests/.btw-history-wrong-format is in a wrong format, remove this file to solve the problem.'
    self.assertEqual(list(filter(lambda err: err == expected_error, user.init()))[0], expected_error)

  # user.get_input()

  def test_get_input(self):
    user = User(['btw', 'list', 'files'], 'tests/.btw-history-good-format')
    self.assertTrue(user.get_input(), "btw list files")

  def test_get_input_empty(self):
    user = User([])
    self.assertFalse(user.get_input())