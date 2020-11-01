import numpy as np

symbols = {}


class Mast:
    action = None
    params = None

    def __init__(self, action=None, params=None):
        self.action = action
        self.params = params

    def execute(self):
        result = None
        if self.action == 'print':
            print(' '.join(str(Mast.resolve(x)) for x in self.params))
        elif self.action == "assign":
            self.assign()
        elif self.action == "arrassign":
            self.arrassign()
        elif self.action == "access":
            if len(self.params[1]) != 2 or not isinstance(self.params[1][0], int) or not isinstance(self.params[1][1],
                                                                                                    int):
                raise SyntaxError
            result = symbols[self.params[0]][self.params[1][0]][self.params[1][1]]
        elif self.action == "binop":
            result = {
                '+': lambda a, b: a + b,
                '-': lambda a, b: a - b,
                '*': lambda a, b: a * b,
                '/': lambda a, b: a / b
            }[self.params[0]](Mast.resolve(self.params[1]), Mast.resolve(self.params[2]))
        elif self.action == "binop_mat":
            result = {
                '.+': lambda a, b: a + b,
                '.-': lambda a, b: a - b,
                '.*': lambda a, b: np.multiply(a, b),
                './': lambda a, b: np.divide(a, b)
            }[self.params[0]](Mast.resolve(self.params[1]), Mast.resolve(self.params[2]))
        elif self.action == "relation":
            result = {
                '>': lambda a, b: (a > b),
                '>=': lambda a, b: (a >= b),
                '<': lambda a, b: (a < b),
                '<=': lambda a, b: (a <= b),
                '==': lambda a, b: (a == b),
                '!=': lambda a, b: (a != b)
            }[self.params[0]](Mast.resolve(self.params[1]), Mast.resolve(self.params[2]))
        elif self.action == "if":
            if Mast.resolve(self.params[0]):
                result = Mast.resolve(self.params[1])
        elif self.action == "ifelse":
            if Mast.resolve(self.params[0]):
                result = Mast.resolve(self.params[1])
            else:
                result = Mast.resolve(self.params[2])
        elif self.action == "while":
            while Mast.resolve(self.params[0]):
                result = Mast.resolve(self.params[1])
                if result == "continue":
                    continue
                if result == "break":
                    break
        elif self.action == "for":
            symbols[self.params[0]] = Mast.resolve(self.params[1])
            while symbols[self.params[0]] <= Mast.resolve(self.params[2]):
                result = Mast.resolve(self.params[3])
                if result == "continue":
                    continue
                if result == "break":
                    break
                symbols[self.params[0]] += 1
        elif self.action == "get":
            result = symbols.get(self.params)
        elif self.action == "execute":
            for instr in self.params:
                result = Mast.resolve(instr)
                if result in ["continue", "break"]:
                    break
        elif self.action == "break":
            result = "break"
        elif self.action == "continue":
            result = "continue"
        elif self.action == "return":
            exit(self.params)
        elif self.action == "uminus":
            result = - Mast.resolve(self.params)
        elif self.action == "trans":
            result = np.transpose(Mast.resolve(self.params))
        elif self.action == "gen":
            result = {
                'zeros': lambda a: np.zeros(shape=[a, a]),
                'ones': lambda a: np.ones(shape=[a, a]),
                'eye': lambda a: np.eye(a)
            }[self.params[0]](Mast.resolve(self.params[1]))
        else:
            print("Error, unsupported operation:", str(self))
        return result

    @staticmethod
    def is_a_delayed_action(x=None):
        return x is not None and isinstance(x, Mast)

    @staticmethod
    def resolve(x):
        if not Mast.is_a_delayed_action(x):
            return x
        else:
            return x.execute()

    def assign(self):
        if self.params[0] == "=":
            symbols[self.params[1]] = Mast.resolve(self.params[2])
        elif self.params[0] == "+=":
            symbols[self.params[1]] = symbols[self.params[1]] + Mast.resolve(self.params[2])
        elif self.params[0] == "-=":
            symbols[self.params[1]] = symbols[self.params[1]] - Mast.resolve(self.params[2])
        elif self.params[0] == "*=":
            symbols[self.params[1]] = symbols[self.params[1]] * Mast.resolve(self.params[2])
        elif self.params[0] == "/=":
            symbols[self.params[1]] = symbols[self.params[1]] / Mast.resolve(self.params[2])

    def arrassign(self):
        if len(self.params[2]) != 2 or not isinstance(self.params[2][0], int) or not isinstance(self.params[2][1], int):
            raise SyntaxError
        if self.params[0] == "=":
            symbols[self.params[1]][self.params[2][0]][self.params[2][1]] = Mast.resolve(self.params[3])
        elif self.params[0] == "+=":
            symbols[self.params[1]][self.params[2][0]][self.params[2][1]] += Mast.resolve(self.params[3])
        elif self.params[0] == "-=":
            symbols[self.params[1]][self.params[2][0]][self.params[2][1]] -= Mast.resolve(self.params[3])
        elif self.params[0] == "*=":
            symbols[self.params[1]][self.params[2][0]][self.params[2][1]] *= Mast.resolve(self.params[3])
        elif self.params[0] == "/=":
            symbols[self.params[1]][self.params[2][0]][self.params[2][1]] /= Mast.resolve(self.params[3])
