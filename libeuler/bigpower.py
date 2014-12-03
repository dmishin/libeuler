from libeuler.numtheor import pow_mod, pfac, gcd, phi
import math

class PowerTower:
    pass

class Int( PowerTower):
    def __init__(self, n):
        assert isinstance(n,int)
        assert n > 0
        self.n=n
    def __str__(self):
        return str(self.n)
    def __repr(self):
        return "Int(%d)"%(self.n)
    def evaluate(self):
        return self.n
    def eval_mod(self, modulus):
        """Evaluate by modulus"""
        return self.n % modulus
    def greater_than(self, x):
        return self.n > x

class Pow( PowerTower ):
    def __init__(self, n, p):
        if isinstance(p, int):
            p = Int(p)
        assert (isinstance(n, int) and isinstance(p, PowerTower))
        self.n=n
        self.p=p
    def __str__(self):
        return "%d**(%s)"%(self.n, self.p)
    def __repr__(self):
        return "Pow(%d,%s)"%(self.n, repr(self.p))

    def greater_than(self, x):
        """n^p > x?"""
        #ln n * p > ln x
        #p > ln x / ln n
        if x < 1: return True
        return self.p.greater_than( math.log(x, self.n))

    def evaluate(self):
        return self.n**self.p.evaluate()        
    def eval_mod(self, modulus):
        """Evaluate by modulus"""
        if isinstance(self.p, Int):
            return pow_mod(self.n, self.p.evaluate(), modulus)
        elif isinstance(self.p, Pow):
            #Most interesting case:
            #Evaluate
            #  n^(m^p) mod modulus
            k = gcd(self.n, modulus)
            n1 = self.n // k #part of N, which is mutually prime with modulus.
            p1 = self.p.eval_mod( phi(modulus) )
            np1 = mod_pow(n1, p1, modulus)

            #Separately: calculate 
            # k**p mod m
            # where m is divisible by k

            for ki, kni in grp(pfaci(self.k)):
                #calcualte ki**(p*kni) mod m,
                #where ki is prime
                
                #How many ki's are in the m?
                mki, modulus1 = divide_completely(modulus, ki)
                assert mki > 0
                #so, m = ki**mki * m1
                #
                # if mki > p*kni, <=> mki/kni > p
                #   then powering will not bring us to the periodic part.
                if not self.p.greater_than( mki / kni ): #true division here!
                    #direct calculation, p is small
                    ki_pow = pow_mod( )
            modfac = grp(pfac(modulus))


def divide_completely( x, y ):
    """Return maximal n such that x % (y**n) == 0,
    and the remaining (x/(y**n)) """
    n = 0
    while x % y == 0:
        x //= x
        n += 1
    return n, x

x = Pow(2, Pow(10, 2))
print(x)
print(x.evaluate())
for y in [2, 3, 4, 5, 1267650600228229401496703205376*2]:
    print ("%s > %d ?: %s"%(x, y, x.greater_than(y)))

print 
