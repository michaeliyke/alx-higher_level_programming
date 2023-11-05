#!/usr/bin/python3


def multiple_returns(sentence):
    if not sentence:
        sentence = ""
    ac = len(sentence)
    ch = sentence[0] if ac > 0 else None
    return ac, ch
