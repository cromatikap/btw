import os, sys, toml

# From: https://www.blog.pythonlibrary.org/2013/10/29/python-101-how-to-find-the-path-of-a-running-script/
FILE_NAME = os.path.abspath(os.path.dirname(sys.argv[0])) + '/btw.toml'

DEFAULT_CONFIG = {
  "OPENAI_API_KEY": "",
  "HISTORY_FILE_NAME": ".btw-history",
  "DEBUG": False
}

def __load_file():
  if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w+") as file:
      file.write(toml.dumps(DEFAULT_CONFIG))
    return DEFAULT_CONFIG
  else:
    return toml.load(FILE_NAME)

def get(var):
  return __load_file()[var]

def set(var, value):
  data = __load_file()
  data[var] = value
  with open(FILE_NAME, "w") as file:
    file.write(toml.dumps(data))
