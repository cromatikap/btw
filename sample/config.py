import toml

def get(var):
  return toml.load('config.toml')[var]