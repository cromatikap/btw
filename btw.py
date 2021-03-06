import sys, AI, toml, debug

def main(argv):
  if(toml.load('config.toml')['DEBUG']):
    debug.p(' [Debug mode] ')

  if(len(argv) <= 1):
    print("Please provide an input, ex: python btw.py turn off the bluetooth")
    return

  user_input = ""
  for i, word in enumerate(argv[1:], start=0):
    if i > 0: user_input += ' '
    user_input += word
  
  print(AI.generate_bash(user_input)[0].text)
  
if __name__ == "__main__":
  main(sys.argv)
