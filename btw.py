import sys, AI, toml, debug
from sample import User

def main(argv):
  user = User(argv)
  user_input = user.parse()
  bash_result = AI.generate_bash(user_input)
  
if __name__ == "__main__":
  main(sys.argv)
