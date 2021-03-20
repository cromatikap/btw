from colored import fg, bg, attr
import toml

#
# format informations displayed when DEBUG = true in config.toml
#

def p(content):
  if(toml.load('config.toml')['DEBUG']):
    color = fg('#FFFFFF') + bg('#00005f')
    res = attr('reset')
    print(color + content + res)
  else:
    pass