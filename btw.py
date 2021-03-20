import sys
from sample.User import User
from sample.History import History
from sample import log, openai

def main(argv):
  log.debug('\n\n [Debug mode] \n')

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
      log.error['arg']('Impossible to connect to OpenAI API, please provide a valid API key using the following command:')
      log.error['arg']('btw --add-openai-key <key>')
  elif(init_status == False):
    log.error['arg']('Please provide an input, ex: python btw.py turn off the bluetooth')
  else:
    log.error['config'](init_status)

def add_openai_key(argv):
  if len(sys.argv) <= 2:
    log.error['arg']('No key provided.')
  else:
    print('Okay.')

if __name__ == "__main__":
  if(len(sys.argv) > 1 and sys.argv[1] == '--add-openai-key'):
    add_openai_key(sys.argv)
  else:
    main(sys.argv)
