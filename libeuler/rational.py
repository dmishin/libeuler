#Python module for simple rational numbers
from libeuler import numtheor
import math

def float2rat(f, eps = None, iters = 1000):
    """Converts float to rational"""
    if eps is None:
        eps = abs(f)*1e-6
    if f < 0:
        return -float2rat(-f, eps, iters)
    flr = math.floor(f)
    frac = f-flr
    if eps<=0:
        raise ValueError("Treshold must be positive")
    
    if iters == 0 or abs(frac)<eps:
        return rat(int(flr),1) #it is actually an integer

    ifrac = 1.0/frac
    
    return rat(int(flr))+1/float2rat(ifrac,eps*ifrac*ifrac, iters-1)

def str2rat(s, base=10):
    """Convert string in a form num/den to a rational. String may be single integer too."""
    spl = s.split("/")
    if len(spl)==1:
        return rat(int(s, base))
    if len(spl)==2:
        return rat( int(spl[0],base), int(spl[1],base) )
    raise ValueError("String is not a fraction: "+s)

def from_confrac( cf ):
    return rat(*numtheor.from_confrac(cf), normalize=False)

class rat:
    "Rational number class"
    
    def __init__(self,num=0,den=1, normalize = True):
        "Create rational value"
        self.num = num
        self.den = den
        if normalize:
            self._norm()
    
    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return "%d/%d"%(self.num, self.den)
    
    def __repr__(self):
        return "rat(%d, %d)"%(self.num, self.den)
    
    def __float__(self):
        return float(self.num)/float(self.den)
    
    def _norm(self):
        "Normalize: remove the common denominator"
        if self.num == 0:
            self.den = 1
        elif self.den == 0:
            #invalud value
            if   self.num < 0:
                self.num = -1
            elif self.num > 0:
                self.num = 1
        elif self.den<0: #normalize sign
            self.num = -self.num
            self.den = -self.den
        else:  
            k = numtheor.gcd(self.num, self.den)
            self.num //= k
            self.den //= k
    
    def intpart(self):
        return self.num//self.den

    def fracpart(self):
        """Fractional part: (4/3).fracpart() == 1/3"""
        return rat(self.num%self.den, self.den, False)

    def copy(self):
        return rat(self.num, self.den, False)
        
    def __mul__(self, v):
        if isinstance(v, int) or isinstance(v, int):
            return rat(self.num*v, self.den)
        if isinstance(v, rat):
            return rat(self.num * v.num, self.den*v.den)
        raise ValueError("Wrong type of multipolier")
    
    def __rmul__(self, v):
        return self.__mul__(v)
        
    def __truediv__(self, v):
        if isinstance(v, int):
            return rat(self.num, self.den*v)
        if isinstance(v, rat):
            return rat(self.num * v.den, self.den*v.num)
        raise ValueError("Wrong type of multipolier")
    
    def __rtruediv__(self, v):
        if isinstance(v, int):
            return rat(self.den*v, self.num)
        if isinstance(v, rat):
            return rat(self.den * v.num, self.num*v.den)
        raise ValueError("Wrong type of multipolier")
        
    def __add__(self, v):
        if isinstance(v, int):
            return rat(self.num+v*self.den, self.den)
        if isinstance(v, rat):
            return rat(self.num * v.den + self.den*v.num, self.den*v.den)
        raise ValueError("Wrong type of second argument: %s"%v)
    def __radd__(self, v):
        return self.__add__(v)

        
    def __pow__(self, v):
        if v > 0:
            return rat(self.num**v, self.den**v, False)
        elif v < 0:
            return rat(self.den**(-v), self.num**(-v), False)
        else:
            return rat(1)
    
    def __sub__(self,v):
        if isinstance(v, int) or isinstance(v, int):
            return rat(self.num-v*self.den, self.den)
        if isinstance(v, rat):
            return rat(self.num * v.den - self.den*v.num, self.den*v.den)
        raise ValueError("Wrong type of second argument: %s"%v)

    def __neg__(self):
        return rat(-self.num, self.den, False)
    def __pos__(self):
        return self
    def __rsub__(self,v):
        "v - rat"
        if isinstance(v, int) or isinstance(v, int):
            return rat(-self.num+v*self.den, self.den)
        if isinstance(v, rat):
            return rat(-self.num * v.den + self.den*v.num, self.den*v.den)
        raise ValueError("Wrong type of second argument: %s"%v)
                
    
    def __abs__(self):
        "absolute value"
        return rat(abs(self.num),abs(self.den),False)

    def iszero (self):
        return self.num == 0
            
    def __eq__(self, v):
        if isinstance(v, rat):
            return self.num*v.den == self.den*v.num
        if isinstance(v, int):
            return self.den*v == self.num
        raise ValueError("Can not compare rational and %s"%v)

    def __le__(self, v):
        if isinstance(v, rat):
            return self.num*v.den <= self.den*v.num
        else:
            return self.num <= self.den*v

    def __ge__(self, v):
        return not self.__lt__(v)

    def __lt__(self, v):
        if isinstance(v, rat):
            return self.num*v.den < self.den*v.num
        else:
            return self.num < self.den*v
    def __gt__(self, v):
        return not self.__le__(v)
    def __hash__(self):
        return (self.num, self.den).__hash__()

    def to_chain(self):
        "Converts rational to chain fraction, that is returned as list."
        return numtheor.confrac(*self.numden())
    
    def from_chain(self, chain):
        "Converts value from chain fraction"
        self.num, self.den = numtheor.from_chain(chain)

    def __int__(self):
        return self.intpart()
    def numden(self):
        return (self.num, self.den)
