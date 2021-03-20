import toml

FILE_NAME = 'config.toml'

def __load_file():
  return toml.load(FILE_NAME)

def get(var):
  return __load_file()[var]

def set(var, value):
  data = __load_file()
  data[var] = value
  with open(FILE_NAME, "w") as file:
    file.write(toml.dumps(data))
