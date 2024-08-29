import sys


def to_morse(message):
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "
    }
    result = ""
    for i in message:
        result += NESTED_MORSE[i]
    return result


def main():
    if (len(sys.argv) != 2):
        print('AssertionError: the arguments are bad')
        sys.exit(1)
    message = sys.argv[1]
    u_message = message.upper()
    for i in u_message:
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 48 and ord(i) <= 57):
            pass
        else:
            print('AssertionError: the arguments are bad')
            sys.exit(1)
    m = to_morse(u_message)
    print(m[:-1])


if __name__ == "__main__":
    main()
