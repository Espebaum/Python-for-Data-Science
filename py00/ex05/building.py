import sys as sys
import string as string


def count(line):
    length = len(line)
    upper, lower, spaces, digits, spaces, digits = 0, 0, 0, 0, 0, 0
    for i in line:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isspace():
            spaces += 1
        elif i.isdigit():
            digits += 1
        elif i.isspace():
            spaces += 1
        elif i.isdigit():
            digits += 1
    punctuation = string.punctuation
    # class str -> "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    punct = [c for c in line if c in punctuation]
    # class list -> ['.']
    print(f'The text contains {length} characters:')
    print(f'{upper} upper letters')
    print(f'{lower} lower letters')
    print(f'{len(punct)} punctuation marks')
    print(f'{spaces} spaces')
    print(f'{digits} digits')
    return 0


def main():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
    elif len(sys.argv) == 1:
        try:
            line = input('What is the text to count?\n')
            count(line)
        except EOFError:
            print('EOF')
            sys.exit(1)
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
            sys.exit(1)
    else:
        str = sys.argv[1]
        count(str)
    return 0


if __name__ == "__main__":
    main()
