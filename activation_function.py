from math import sqrt, exp

def polynome_specialisation(x, coefs):
    '''
    Horner algorithm
    '''
    value = 0
    for c in reversed(coefs):
        value *= x
        value += c
    return value

def bentIdentity(x):
    return (np.sqrt(x*x + 1) - 1) / 2 + x

def sigmoid(x):
    return 1 / (1 + exp(-x))

def approx_bentIdentity(x):
    '''
    Interpolation over [-10, 10].spécialisation polynome
    Ref:https://mortendahl.github.io/2017/04/17/private-deep-learning-with-mpc/#approximating-sigmoid
    '''
    coefs = [0.0643856681, 1.0, 0.1423387434, 0.0, -0.0039900774, 0.0, 7.60809e-5, 0.0, -7.114e-07, 0.0, 2.5e-9 ]
    return polynome_specialisation(x, coefs)

def approx_sigmoid(x):
    '''
    Interpolation over [-10, 10].
    Ref:https://mortendahl.github.io/2017/04/17/private-deep-learning-with-mpc/#approximating-sigmoid
    '''
    coefs = [1/2, 0.2159198015, 0, -0.0082176259, 0, 0.0001825597, 0, -0.0000018848, 0, 0.0000000072]
    return polynome_specialisation(x, coefs)

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    #Bent Identity
    X = np.arange(-10, 10, 0.1)
    y_bent = [bentIdentity(x) for x in X]
    y_bent_approx = [approx_bentIdentity(x) for x in X]
    plt.plot(X, y_bent, label="bentIdentity")
    plt.plot(X, y_bent_approx, label="interpolated bentIdentity")

    #Sigmoid
    y_sig = [sigmoid(x) for x in X]
    y_sig_approx = [approx_sigmoid(x) for x in X]
    plt.plot(X, y_sig, label="sigmoid")
    plt.plot(X, y_sig_approx, label="interpolated sigmoid")

    plt.xlabel('x - axis') 
    plt.ylabel('y - axis') 
    plt.title('Real and interpolated activations functions') 
    plt.legend()
    plt.show()



