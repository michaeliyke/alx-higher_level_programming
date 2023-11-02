#!/usr/bin/python3

import hidden_4 as h

arr = sorted(dir(h))
if __name__ == "__main__":
  for e in arr:
    if not e.startswith("_"):
      print("{}".format(e))
