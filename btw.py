import sys
from sample.user import User
from sample import debug, AI

def main(argv):

  user = User(argv)
  user_input = user.get_input()

  if(user_input):
    bash_result = AI.generate_bash(user_input)
    print('\n$ ' + bash_result + '\n')
    feedback = user.set_feedback()

    if (feedback == 'Execute'):
      user.execute(bash_result)
    elif (feedback == 'Correct'):
      user.execute(user.correct(bash_result))
    elif (feedback == 'Cancel'):
      pass
  else:
    print("Please provide an input, ex: python btw.py turn off the bluetooth")
  
if __name__ == "__main__":
  main(sys.argv)
