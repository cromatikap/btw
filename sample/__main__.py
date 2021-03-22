from sample.User import User
from sample.History import History
from sample import log, openai, config

def main(argv):
  if(len(argv) > 1 and argv[1] == '--add-openai-key'):
    __add_openai_key(argv)
  else:
    __run(argv)

def __run(argv):
  log.debug('      [Debug mode]      ')

  user = User(argv)
  init_status = user.init()
  if(init_status == True):
    user_input = user.get_input()

    bash_result = openai.generate_bash(user_input)
    # DEBUG:
    # bash_result = "ls -l"

    if(bash_result):
      print('\n$ ' + bash_result + '\n')
      feedback = user.set_feedback()

      if (feedback == 'Execute'):
        user.execute(bash_result)
      elif (feedback == 'Correct'):
        user.execute(user.correct(bash_result))
      elif (feedback == 'Cancel'):
        pass
    else:
      print('\nUsage: btw --add-openai-key <key>\n')
  elif(init_status == False):
    log.error['arg']('Please provide an input, ex: python btw.py turn off the bluetooth')
  else:
    log.error['config'](init_status)

def __add_openai_key(argv):
  if len(argv) <= 2:
    log.error['arg']('No key provided.')
  else:
    config.set('OPENAI_API_KEY', argv[2])
    print('OpenAI API Key added.')