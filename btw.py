import sys
from sample.User import User
from sample.History import History
from sample import debug, openai, error

def main(argv):
  debug.p('\n\n [Debug mode] \n')

  user = User(argv)
  config_status = user.check_config()
  if(config_status == True):
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
      error.arg('Impossible to connect to OpenAI API, please provide a valid API key using the following command:')
      error.arg('btw --add-openai-key <key>')
  elif(config_status == False):
    error.arg('Please provide an input, ex: python btw.py turn off the bluetooth')
  else:
    error.config(config_status)
  
if __name__ == "__main__":
  main(sys.argv)
