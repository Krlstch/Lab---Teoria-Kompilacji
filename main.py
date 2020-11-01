import sys
import scanner
import Mparser
from mast import Mast

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "test.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = Mparser.parser
    text = file.read()
    prog = parser.parse(text, lexer=scanner.lexer, debug=1)
    for x in prog:
        Mast.resolve(x)
