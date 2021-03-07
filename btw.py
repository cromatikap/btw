import sys
from sample.user import User
from sample import debug, AI

def main(argv):
  user = User(argv)
  user_input = user.get_input()
  bash_result = AI.generate_bash(user_input)
  print(bash_result)
  
if __name__ == "__main__":
  main(sys.argv)
