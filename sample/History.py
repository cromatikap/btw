import csv
from sample import log, config

HISTORY_FILE_PATH = config.get('HISTORY_FILE_NAME')

class History:

  def __init__(self, file_path_name=HISTORY_FILE_PATH):
    self.file_path_name = file_path_name
    try:
      f = open(file_path_name, 'x')
      log.debug(file_path_name + ' file created.')
      f.close()
    except:
      log.debug(file_path_name + ' file found.')
    finally:
      self.file = open(file_path_name, 'r+')
  
  def __del__(self):
    self.file.close()

  def __has_wrong_format(self, file):

    reader = csv.reader(file, delimiter=',', quotechar='|')
    for row in reader:
      if(len(row) != 2):
        return True
    return False
  
  def error(self):
    if(self.__has_wrong_format(self.file)):
      return self.file_path_name + ' is in a wrong format, remove this file to solve the problem.'
    else:
      return False
  
  def __find_by_input(self, txt_input):
    log.debug(self.__class__.__name__ + '.__find_by_input("' + txt_input + '"):')
    reader = csv.reader(self.file, delimiter=',', quotechar='|')
    for row in reader:
      if(row[0] == txt_input):
        log.debug('Found: ' + row[0] + ' => ' + row[1])
        return row[1]
        break
    log.debug('"' + txt_input + '" not found in local history.')
    return False

  def __find_by_output(self, output):
    pass
  
  def save(self, txt_input, txt_output):
    log.debug(self.__class__.__name__ + '.save("' + txt_input + '", "' + txt_output + '"):')
    if(self.__find_by_input(txt_input)):
      log.debug('Already saved in history.')
    else:
      log.debug('Add "' + txt_input + '" => "' + txt_output + '" to local history.')