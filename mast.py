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
            print(' '.join(str(Mast.resolve(x)) for x in list(self.params)))
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
