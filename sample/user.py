import toml, inquirer, subprocess
from sample import debug

class User:
  def __init__(self, input):
    self.input = input
  
  def get_input(self):
    if(toml.load('config.toml')['DEBUG']):
      debug.p(' [Debug mode] ')

    if(len(self.input) <= 1):
      print("Please provide an input, ex: python btw.py turn off the bluetooth")
      return

    input = ""
    for i, word in enumerate(self.input[1:], start=0):
      input += ' ' + word

    return input.strip()
  
  def set_feedback(self):
    answers = inquirer.prompt([
      inquirer.List(
        "action",
        message="Your choice",
        choices=["Execute", "Correct", "Cancel"],
      ),
    ])
    return answers['action']
  
  def execute(self, bash_command):
    result = subprocess.run(bash_command.split(), stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8').strip())
    
    if(result.stderr):
      print('[error]')
      print(result.stderr)
  
  def correct(self):
    print('Correct: coming soon.')