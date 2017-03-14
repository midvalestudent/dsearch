''' main hashing functions
'''
import string
from collections import defaultdict

import numpy as np
try:
    from pyfftw.interfaces.scipy_fftpack import dct
except ImportError:
    from scipy.fft import dct


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
    def __init__(self, d, m, h, ord=None, random_state=np.random.RandomState(42)):
        if m%d:
            raise ValueError("m must be an integer multiple of d")

        super(FourierHasher, self).__init__(h, m, ord)
        self.signs = random_state.choice([-1.0, 1.0], size=(m/d, d))
        self.sqrt_d = np.sqrt(d)

    def transform(self, vector):
        return dct(np.multiply(self.signs, vector).flatten(), type=2, norm='ortho')*self.sqrt_d
