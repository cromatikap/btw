import toml
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
      if i > 0: input += ' '
      input += word

    return input