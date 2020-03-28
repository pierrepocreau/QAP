
class Wire:

    def __init__(self, value, in_gate):
        self.value = value
        self.in_gate = in_gate
    
    def connect_exit(self, gate):
        self.out_gate = gate
        
