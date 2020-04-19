from wire import Wire
from gates import Mult, Add, MultScalar

def bentIdentity(X):
    '''
    Activation function bring non-linearities and multiplications gates.
    f(x) = (sqrt(x^2 + 1) -1) / 2 + x
    '''

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