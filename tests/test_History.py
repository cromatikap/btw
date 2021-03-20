import unittest
from sample.History import History

class TestUser(unittest.TestCase):

  def test_check_file_good_format(self):
    history = History('tests/.btw-history-good-format')
    self.assertIs(history.check_file(), True)
  
  def test_check_file_wrong_format(self):
    history = History('tests/.btw-history-wrong-format')
    self.assertEqual(history.check_file(), 'tests/.btw-history-wrong-format is in a wrong format, remove this file to solve the problem.')
