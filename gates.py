from wire import Wire

class Mult:

    def __init__(self, wire1, wire2):
        self.wire1 = wire1
        self.wire2 = wire2
        self.output = Wire(wire1.value * wire2.value, self)

class Add:

    def __init__(self, wire1, wire2):
        self.wire1 = wire1
        self.wire2 = wire2
        self.output = Wire(wire1.value + wire2.value, self)

class MultScalar:

    def __init__(self, wire, scalar):
        self.wire = wire
        self.scalar = scalar
        self.output = Wire(wire.value * scalar, self)
