import csv
from sample import debug

class History:

  def __init__(self, file_path_name=".btw-history"):
    debug.p(self.__class__.__name__ + '.__init__()')
    self.file_path_name = file_path_name
    try:
      f = open(file_path_name, 'x')
      f.close()
    except:
      debug.p(file_path_name + ' file found.')
    finally:
      self.file = open(file_path_name, 'r+')
  
  def __del__(self):
    debug.p(self.__class__.__name__ + '.__del__()')
    self.file.close()

  def __has_wrong_format(self, file):

    reader = csv.reader(file, delimiter=',', quotechar='|')
    for row in reader:
      if(len(row) != 2):
        return True
    return False
  
  def check_file(self):
    if(self.__has_wrong_format(self.file)):
      return self.file_path_name + ' is in a wrong format, remove this file to solve the problem.'
    else:
      return True
  
  def __find_by_input(self, txt_input):
    debug.p(self.__class__.__name__ + '.__find_by_input("' + txt_input + '"):')
    reader = csv.reader(self.file, delimiter=',', quotechar='|')
    for row in reader:
      if(row[0] == txt_input):
        debug.p('Found: ' + row[0] + ' => ' + row[1])
        return row[1]
        break
    debug.p('"' + txt_input + '" not found in local history.')
    return False

  def __find_by_output(self, output):
    pass
  
  def save(self, txt_input, txt_output):
    debug.p(self.__class__.__name__ + '.save("' + txt_input + '", "' + txt_output + '"):')
    if(self.__find_by_input(txt_input)):
      debug.p('Already saved in history.')
    else:
      debug.p('Add "' + txt_input + '" => "' + txt_output + '" to local history.')