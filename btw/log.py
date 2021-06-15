from colored import fg, bg, attr
from . import config

#
# format informations displayed when DEBUG = true in config.toml
#

def debug(content):
  if(config.get('DEBUG')):
    color = fg('#FFFFFF') + bg('#00005f')
    print(color + content + attr('reset'))
  else:
    pass

def error_config(messages):
  if(len(messages) > 0):
    print('\n                      [ Configuration error ]\n')
    for msg in messages:
      print(' -> ' + str(msg))
      print()

def error_arg(message):
  color = fg('#FF0000')
  print(color + message + attr('reset'))

error = {
  'arg': error_arg,
  'config': error_config
}