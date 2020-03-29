from wire import Wire
from gates import Mult, Add, MultScalar

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

    inputs, outputs = matVec_AC(A, X)
    resultats = [output.value for output in outputs]
    print(resultats)