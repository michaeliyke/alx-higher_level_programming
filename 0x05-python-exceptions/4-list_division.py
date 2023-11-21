#!/usr/bin/python3


def list_division(L1, L2, lnth):
    arr = []
    for i in range(lnth):
        try:
            a, b = L1[i], L2[i]
            r = a / b
        except ZeroDivisionError:
            print("division by zero")
            r = 0
        except IndexError:
            print("out of range")
            r = 0
        except TypeError:
            print("wrong type")
            r = 0
        except Exception:
            r = 0
        finally:
            arr.append(float(r) if r != 0 else r)
    return arr
