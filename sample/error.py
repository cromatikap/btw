def config(messages):
  if(len(messages) > 0):
    print('\n                      [ Configuration error ]\n')
    for msg in messages:
      print(' -> ' + str(msg))
      print()

def arg(message):
  print(message)