from wire import Wire
from gates import Mult, Add, MultScalar

# RECURSIVE FUNCTION, No more than 1000 calls...
# Maybe we could use generator instead of lists.
def polynome_AC(x, coefs):
    '''
    Arithmetic circuit for P(x) where P is a polyome.
    '''
    def aux(inputs, coefs):
        coef = Wire(coefs.pop(), None)

        if len(coefs) == 0:
            return coef
        
        mult_gate = Mult(inputs[-1], aux(inputs[:-1], coefs))
        inputs[-1].connect_exit(mult_gate)
        return Add(coef, mult_gate.output).output

    power = len(coefs) - 1
    inputs = [Wire(x, None) for _ in range(power)] # As many input as deg(P)
    #reverse so we use pop() instead of pop(0)
    copy = coefs.copy()
    copy.reverse()
    return inputs, aux(inputs, copy)

def polyVec(X, coefs):
    pass

def polyMat(X, coefs):
    '''
    Arithmetic circuit for P(X) where X is a matrice and P a polynome.
    '''
    inputs_X, outputs = [], []
    for line in X:
        input_line, output_line = [], []
        for x in line:
            inputs, output = polynome_AC(x, coefs)
            input_line.append(inputs)
            output_line.append(output)
        
        inputs_X.append(input_line)
        outputs.append(output_line)
    return inputs_X, outputs


def matMat_AC(A, B):
    '''
    Arithmetic circuit for Matrix * Matrix multiplication
    '''
    n, k = len(A), len(A[0])
    m = len(B[0])
    inputs, outputs = [], []
    B_col = list(zip(*B))

    for j in range(m):
        input_, output = matVec_AC(A, B_col[j])
        inputs.append(input_)
        outputs.append(output)

    #list(zip(*A)) take the transpose of A
    return list(zip(*inputs)), list(zip(*outputs))

def matVec_AC(A, X):
    '''
    Arithmetic circuit for Matrice * Vector multiplication.
    '''
    n, k = len(A), len(A[0])
    inputs = [Wire(x, None) for x in X]
    outputs = [None for _ in range(n)]
    
    for j in range(n):
        outputs[j] = vecVec_AC(A[:][j], inputs)
    
    return inputs, outputs

# RECURSIVE FUNCTION, No more than 1000 calls...
def vecVec_AC(A, inputs):
    '''
    Arithmetic circuit for vector * vector multiplication.
    Y * X = Y[-1] * X[-1] + Y[:-1] * X[:-1]
                       ADD
                    /       \
                MultScal     Rec
                /      \
              Y[-1]     X[-1]
    '''
    n = len(A)
    if n == 1:
        gate = MultScalar(inputs[0], A[0])
        inputs[0].connect_exit(gate)
        return gate.output
    else:
        gate = MultScalar(inputs[-1], A[-1])
        inputs[-1].connect_exit(gate)
        return Add(gate.output, vecVec_AC(A[:-1], inputs[:-1])).output

if __name__ == "__main__":
    A = [[2, 4, 1], [5, 2, 2]]
    X = [1, 2, 3]
    B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    inputs, outputs = matVec_AC(A, X)
    inputs2, outputs2 = matMat_AC(A, B)

    resultats = [output.value for output in outputs]
    resultats2 = [[output.value for output in ligne] for ligne in outputs2]
    print(resultats)
    print(resultats2)

    poly = [1, 2, 1, 2, 0, 5]
    inputs, calc = polynome_AC(2, poly)
    print(calc.value)
    print(inputs)

    inputs, outputs = polyMat(A, poly)
    resultats = [[output.value for output in ligne] for ligne in outputs]
    print(resultats)
    print(inputs)