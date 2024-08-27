import sys as sys


def whatis():
    if len(sys.argv) < 2:
        sys.exit(1)
    # assert len(sys.argv) == 2, 'more than one argument is provided'
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
    try:
        val = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(1)
    if val % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")


whatis()
