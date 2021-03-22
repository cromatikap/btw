import sys, os
from sample.__main__ import main

# From: https://stackoverflow.com/a/47699138/12596275
def override_where():
  """ overrides certifi.core.where to return actual location of cacert.pem"""
  # change this to match the location of cacert.pem
  return os.path.abspath("cacert.pem")

# is the program compiled?
if hasattr(sys, "frozen"):
  import certifi.core

  os.environ["REQUESTS_CA_BUNDLE"] = override_where()
  certifi.core.where = override_where

  # delay importing until after where() has been replaced
  import requests.utils
  import requests.adapters
  # replace these variables in case these modules were
  # imported before we replaced certifi.core.where
  requests.utils.DEFAULT_CA_BUNDLE_PATH = override_where()
  requests.adapters.DEFAULT_CA_BUNDLE_PATH = override_where()

if __name__ == '__main__':
  main(sys.argv)
