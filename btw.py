import sys
from sample.User import User
from sample.History import History
from sample import debug, openai

def main(argv):
  debug.p('\n\n [Debug mode] \n')

  user = User(argv)
  config_status = user.check_config()
  if(config_status == True):
    user_input = user.get_input()

    bash_result = openai.generate_bash(user_input)
    # DEBUG:
    # bash_result = "ls -l"

    print('\n$ ' + bash_result + '\n')
    feedback = user.set_feedback()

    if (feedback == 'Execute'):
      user.execute(bash_result)
    elif (feedback == 'Correct'):
      user.execute(user.correct(bash_result))
    elif (feedback == 'Cancel'):
      pass
  else:
    print('\n                      [ Configuration error ]\n')
    print(config_status)
    print()
  
if __name__ == "__main__":
  main(sys.argv)
