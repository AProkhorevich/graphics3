from numpy import choose
from line import line
from circle import circle


if __name__ == '__main__':
    while True:
        choice = input('choose one:\n1. Circle\n2. Line\n')
        try:
            choice = float(choice)
        except:
            print("choose 1 or 2")
            continue

        if choice == 1:
            circle()
        if choice == 2:
            line()
