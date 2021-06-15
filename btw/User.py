import sys, inquirer, subprocess, readline
from .History import History
from . import log, config

class User:
  def __init__(self, txt_input, history_path_name = None):
    self.txt_input = txt_input
    self.History = History(history_path_name) if history_path_name else History()
  
  def init(self):
    errors = []
    if(self.get_input()):

      history_error = self.History.error()
      if(history_error):
        errors.append(history_error)

      if(len(config.get('OPENAI_API_KEY')) == 0):
        errors.append('OpenAI API key has not been provided. Please run the following command:\n    btw --add-openai-key <key>')

      if(errors):
        return errors
      else:
        return True
    else:
      return False
  
  def get_input(self):

    if(len(self.txt_input) <= 1):
      return False

    txt_input = ""
    for i, word in enumerate(self.txt_input[1:], start=0):
      txt_input += ' ' + word

    return txt_input.strip()
  
  def set_feedback(self):
    answers = inquirer.prompt([
      inquirer.List(
        "action",
        message="Your choice",
        choices=["Execute", "Correct", "Cancel"],
      ),
    ])
    return answers and answers['action']
  
  def execute(self, bash_command):

    bash_command = bash_command.strip()

    print(' [ Execute ] $ ' + bash_command)
    result = subprocess.run(bash_command.split(), stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8').strip())

    self.History.save(self.get_input(), bash_command)
    
    if(result.stderr):
      print(' [ error ] ')
      print(result.stderr)

  def correct(self, placeholder):
    
    def rlinput(self, prefill=''):
      readline.set_startup_hook(lambda: readline.insert_text(prefill))
      try:
        return input(self)
      finally:
        readline.set_startup_hook()

    correction = rlinput(' [ Correct ] $ ', placeholder)

    return correction
    