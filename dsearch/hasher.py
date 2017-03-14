''' main hashing functions
'''
import string
from collections import defaultdict

import numpy as np


def symbol_encode(n, symbols):
    nb_symbols = len(symbols)
    
    if n < nb_symbols:
        return symbols[n]
    
    retval = ''
    while n > 0:
        n, k = divmod(n, nb_symbols)
        retval += symbols[k]

    return retval


def normalize(v, ord=2):
    norm = np.linalg.norm(v, ord=ord)
    if not norm:
        return v
    inv_norm = 1./norm
    return inv_norm*v


class HashGenerator(object):
    def __init__(self, symbols=None):
        self.curr = 0
        self.symbols = symbols
        if self.symbols is None:
            self.symbols = string.digits+string.lowercase

    def __call__(self):
        retval = symbol_encode(self.curr, self.symbols)
        self.curr += 1
        return retval


class ThresholdingHasher(object):
    def __init__(self, h, m, ord=None):
        self.h = h
        self.m = m
        self.hashes = defaultdict(HashGenerator())
        self.ord = ord

    @property
    def r(self):
        return 0.5*self.h**2/np.log(self.m)
    
    def encode(self, vector):
        if self.ord:
            vector = normalize(vector, self.ord)
        u = self.transform(vector)
        keys = np.flatnonzero(u>self.h)
        return [self.hashes[k] for k in keys]


class GaussianHasher(ThresholdingHasher):
    def __init__(self, d, m, h, ord=None, random_state=np.random.RandomState(42)):
        super(GaussianHasher, self).__init__(h, m, ord)
        self.matrix = random_state.normal(size=(m, d))

    def transform(self, vector):
        return self.matrix.dot(vector)


class FourierHasher(ThresholdingHasher):
    ''' Approximate the random Gaussian mapping by a sparse operation followed
        by a Fourier transform.

        The vector is duplicated m/d times, and each element of the duplicated
        vector is multiplied randomly by +1 or -1.  These duplicated vectors are
        concatenated and then their DFT is returned.  This entire operation
        approximates multiplication of the vector by a standard normal Gaussian 
        m x d matrix.

        Note that a dct implementation must be provided to the constructor.  Two
        options are:

            * scipy.fft.dct
            * pyfftw.interfaces.scipy_fftpack.dct

        See: https://arxiv.org/abs/1507.05929
    '''
    def __init__(self, d, m, h, ord=None, dct=None, random_state=np.random.RandomState(42)):
        if m%d:
            raise ValueError("m must be an integer multiple of d")

        super(FourierHasher, self).__init__(h, m, ord)
        self.signs = random_state.choice([-1.0, 1.0], size=(m/d, d))
        self.sqrt_d = np.sqrt(d)

        self.dct = dct
        if not self.dct:
            raise NotImplementedError("a dct implmentation must be provided")

    def transform(self, vector):
        return self.dct(np.multiply(self.signs, vector).flatten(), type=2, norm='ortho')*self.sqrt_d
