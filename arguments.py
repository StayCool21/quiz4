import argparse 

def hello() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(help='Enter a string', dest='word', type=str)
    parser.add_argument(help='Enter an integer', dest='num', type=int)
    parser.add_argument(help='Enter a float', dest='decimal', type=float)

    args = parser.parse_args()

    string = args.word
    integer = args.num
    decimal = args.decimal

    print('String entered:', string)
    print('Integer entered:', integer)
    print('Float entered:', decimal)

if __name__ == '__main__':
    hello()