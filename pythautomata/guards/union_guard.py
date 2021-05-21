from pythautomata.base_types.symbol import Symbol
from  pythautomata.base_types.guard import Guard

class UnionGuard(Guard):
    def __init__(self, *guards:Guard):
        self.guards = list(guards)

    def matches(self, s:Symbol):
        return any(map(lambda g: g.matches(s), self.guards))

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return print(*self.guards, sep=u" \u222A ")