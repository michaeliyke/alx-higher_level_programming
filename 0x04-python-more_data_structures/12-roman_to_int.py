#!/usr/bin/python3
bv = {
    1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
    90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M",
    }

bv = {
    "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50,
    "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000,
    }

# I, X, C, M
def thousands(s):
    count = 0
    for i in s:
        if i != "M":
            break
        count += 1
    return count

def hundredths(s):
    count = 0
    for i in s:
        if i != "C":
            break
        count += 1
    return count

def tens(s):
    count = 0
    for i in s:
        if i != "X":
            break
        count += 1
    return count


def units(s):
    count = 0
    for i in s:
        if i != "I":
            break
        count += 1
    return count


def roman_to_int(rs):
    """converts a Roman numeral to an integer"""

    total = 0
    # collect 1000s
    count = thousands(rs)
    total += 1000 * count
    rs = rs[count:]

    # ccollect 900
    if len(rs) >= 2 and rs[0:2] == "CM":
        rs = rs[2:]
        total += 900

    # collect 500
    if len(rs) >= 1 and rs[0] == "D":
        rs = rs[1:]
        total += 500

    # collect 400
    if len(rs) >= 2 and rs[0:2] == "CD":
        rs = rs[2:]
        total += 400

    #TODO: collect 100s
    count = hundredths(rs)
    total += 100 * count
    rs = rs[count:]

    # collect 90
    if len(rs) >= 2 and rs[0:2] == "XC":
        rs = rs[2:]
        total += 90

    # collect 50
    if len(rs) >= 1 and rs[0] == "L":
        rs = rs[1:]
        total += 50

    # collect 40
    if len(rs) >= 2 and rs[0:2] == "XL":
        rs = rs[2:]
        total += 40

    #TODO: collect 10s
    count = tens(rs)
    total += 10 * count
    rs = rs[count:]

    # collect 9
    if len(rs) >= 2 and rs[0:2] == "IX":
        rs = rs[2:]
        total += 9

    # collect 5
    if len(rs) >= 1 and rs[0] == "V":
        rs = rs[1:]
        total += 5

    # collect 4
    if len(rs) >= 2 and rs[0:2] == "IV":
        rs = rs[2:]
        total += 4

    #TODO:  collect 1s
    count = units(rs)
    total += 1 * count
    rs = rs[count:]
    return total
