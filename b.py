class NestedContexts:
    def __init__(self, *contexts):
        self._enters = []
        self._exits = []
        self._values = []
        for ctx in contexts:
            self._enters.append(ctx.__enter__)
            self._exits.append(ctx.__exit__)

    def __enter__(self):
        for enter in self._enters:
            self._values.append(enter())
        return self._values

    def __exit__(self, typ, val, tb):
        for exit in self.exits[::-1]:
            exit(typ,val,tb)
        return False
