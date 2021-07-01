from tempfile import NamedTemporaryFile
import csv, shutil
from . import log, config

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
    reader = csv.reader(file, delimiter=',')
    for row in reader:
      if(len(row) != 2):
        return True
    return False
  
  def error(self):
    if(self.__has_wrong_format(self.file)):
      return self.file_path_name + ' is in a wrong format, remove this file to solve the problem.'
    else:
      return False

  def save(self, txt_input, txt_output):
    log.debug(self.__class__.__name__ + '.save("' + txt_input + '", "' + txt_output + '"):')
    tempfile = NamedTemporaryFile('w+t', delete=False)

    with open(self.file_path_name, 'r') as csvFile, tempfile:
      edited = False
      reader = csv.reader(csvFile, delimiter=',')
      writer = csv.writer(tempfile, delimiter=',')

      for row in reader:
        if(row[0] == txt_input):
          row[1] = txt_output
          edited = True
        writer.writerow(row)
      
      if not edited:
        writer.writerow([txt_input, txt_output])
      
    shutil.move(tempfile.name, self.file_path_name)
  
  def get_q_and_a(self):
    output = ""
    self.file.seek(0)
    reader = csv.reader(self.file, delimiter=',')
    for row in reader:
      output += "\nQ: " + row[0] + "\nA: " + row[1]
    return output