import unittest
from btw.History import History

class TestHistory(unittest.TestCase):

  def test_check_file_good_format(self):
    history = History('tests/.btw-history-good-format')
    self.assertIs(history.error(), False)
  
  def test_check_file_wrong_format(self):
    history = History('tests/.btw-history-wrong-format')
    self.assertEqual(history.error(), 'tests/.btw-history-wrong-format is in a wrong format, remove this file to solve the problem.')
