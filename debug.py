from colored import fg, bg, attr

#
# printd() => print_debug(), format informations displayed when DEBUG = true in config.toml
#

def p(content):
  color = fg('#C0C0C0') + bg('#00005f')
  res = attr('reset')
  print(color + content + res)