import sys
from sample.user import User
from sample import debug, AI

def main(argv):

  user = User(argv)
  bash_result = AI.generate_bash(user.get_input())
  # bash_result = 'ls -la' # <- DEBUG

  print('\n$ ' + bash_result + '\n')
  feedback = user.set_feedback()

  if (feedback == 'Execute'):
    user.execute(bash_result)
  elif (feedback == 'Correct'):
    user.execute(user.correct(bash_result))
  elif (feedback == 'Cancel'):
    pass
  
if __name__ == "__main__":
  main(sys.argv)
