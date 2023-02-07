import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # positional args
    parser.add_argument("number1", help="First number")
    parser.add_argument("number2", help="second number")
    parser.add_argument("operation", help="operation")
    # optionsal args
    parser.add_argument('--path', help="provide path to store the result")
    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)
