#!/usr/bin/python3

import hidden_4 as h

if __name__ == "__main__":
  for e in dir(h):
    if not e.startswith("_"):
      print("{}".format(e))
