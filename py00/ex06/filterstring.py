import sys as sys


def count(w, condition):
    words = w.split()
    result = [word for word in words if condition(word)]
    return result


def main():
    arg_len = len(sys.argv)
    if arg_len != 3:
        print('AssertionError: the arguments are bad')
        sys.exit(1)
    words = sys.argv[1]
    length = sys.argv[2]

    nu = 0
    for i in length:
        k = ord(i)
        if k < 48 or k > 57:
            print('AssertionError: the arguments are bad')
            sys.exit(1)
        nu = nu * 10 + (k - 48)
    result = count(words, lambda x: len(x) > nu)
    print(result)


if __name__ == "__main__":
    main()


# first-class function, lambda function, list comprehension
