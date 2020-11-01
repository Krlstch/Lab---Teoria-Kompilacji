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
        elif self.action == "binop":
            result = {
                '+':  lambda a, b: a + b,
                '-':  lambda a, b: a - b,
                '*':  lambda a, b: a * b,
                '/':  lambda a, b: a / b
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
                Mast.resolve(self.params[1])
        elif self.action == "for":
            symbols[self.params[0]] = Mast.resolve(self.params[1])
            while symbols[self.params[0]] != Mast.resolve(self.params[2]):
                Mast.resolve(self.params[3])
                symbols[self.params[0]] += 1
        elif self.action == "get":
            result = symbols.get(self.params[0])
        elif self.action == "execute":
            for instr in self.params:
                Mast.resolve(instr)
        elif self.action == "uminus":
            result = - Mast.resolve(self.params)
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
