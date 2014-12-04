import math
from functools import reduce

def isprime(x):
    "Check, whether the numer is prime. Complexity ~sqrt(p)/2"
    if x<2:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    for p in range(3,sqrti(x)+1,2):
        if x%p==0:
            return False
    return True

def primes_gen():
    "Infinite sequence of primes. Not effective for big sizes, use primes(n) instead."
    yield(2)
    p=3
    while True:
        if isprime(p):
            yield p
        p+=2

def primes_gen_table():
    """Infinite sequence of primes. 
    Uses table of primes to improve performance for large numbers"""
    ps = [2,3,5,7,11,13,17,19,23]
    yield from ps
    
    x = ps[-1]
    while True:
        x += 2
        for d in ps:
            if d*d > x:
                #it's prime!
                yield x
                ps.append(x)
                break
            if x % d == 0:
                break #not a prime
        
def primes(n):
    "Table of prime numbers below n. Uses seive."
    seive=[True]*n
    seive[0],seive[1]=False,False
    def strikeout(i):
        for j in range(i*2,n,i):
            seive[j]=False
    for i in range(n):
        if seive[i]:
            strikeout(i)
    return [ p for p, isp in enumerate(seive) if isp ]




def countstep(x=0,step=1):
    "like itertools.count, but step can be specified"
    while True:
        yield x
        x=x+step    

def pfac(x):
    "Prime factorization"
    return list(pfaci(x))
            
def pfaci(x):
    "Prime factorization generator version"
    def nums():
        yield 2
        for p in countstep(3,2):
            yield p
    
    for p in nums():
        if x<=1:
            return
        while x%p==0:
            x = x//p
            yield p
            
def pfac_table(x, table):
    """Use primes table to factor the integer.
    Table must be sorted.
    Generates sequence of the prime factors in increasing order;
    Result will conicide with pfaci, if the biggest number in the table is bigger than x^2
    """
    pbiggest = table[-1]
    for p in table:
        while x % p == 0:
            x //= p
            yield p
        if p*p > x:
            break
    if x > 1:
        yield x
                
def grp(l):
    "groups list"
    v=None
    n=-1
    for y in l:
        if n==-1:#if first
            v=y
            n=1
        else:
            if y==v:
                n+=1
            else:
                yield (v,n)
                v=y
                n=1
    if v is not None:
        yield (v,n)

def numdivs(n, factorize = pfaci):
    """number of divisors.
    Allows to use custom factorizer
    """
    if n==1: return 1
    return prod(e+1 for _,e in grp(factorize(n)) )

def findfirst(l, pred):
    "Finds first item in sequence, that makes the predicate true"
    for y in l:
        if pred(y):
            return y

def pow_mod(x,n,p):
    "returns x^n mod p"
    def sqr(x):
        return (x*x)%p
    def pow(w,n):
        if n==0:
            return 1
        if n==1:
            return x%p
        if n%2==0:
            return sqr(pow(x,n/2))
        else:
            return (sqr(pow(x,n/2))*x)%p
    return pow(x,n)




def mrange(begins, ends=None, steps=None):
    """Multidimensional range. 
    mrange ( ends )
    mrange ( begins, ends )
    mrange ( begins, ends, steps )

    Generates sequence of tuples,
    sorting order is inverse lexicographic!
    
    mrange( (3,2) )
    generates:
     [ (0,0), (1,0), (2,0), (0,1), (0,2), (0,3) ]
    """
    if steps is None:
        steps=(1,)*len(begins)
    if ends is None:
        ends=begins
        begins=(0,)*len(ends)
        
    if len(begins)!=len(ends) or len(ends)!=len(steps):
        raise ValueError("Begins, ends, steps must have the same length")

    return __mrange_rec(list(zip(begins,ends,steps)))

def __mrange_rec(bes):
    """Implementation of the mrange
    arguments: list of tuples [ (begin, end, step) ]
    """
    if len(bes)==0:
        return
    elif len(bes)==1:
        for x in range(*(bes[0])):
            yield (x,)
    else:
        for x2_xn in __mrange_rec(bes[1:]):
            for x1 in range(*(bes[0])):
                yield (x1,)+x2_xn
                

def prod(l, initial=1):
    "Product of all items in list"
    p = initial
    for x in l:
        p *= x
    return p

def alldivs(x, factorize = pfaci):
    """generates all divisors of x, including 1 and the number itself.
    Order is not increasing!"""
    if x == 1:
        yield 1
        return

    decomp=tuple(grp(factorize(x)))    
    #enumerate all powers
    P=[p for p,e in decomp]
    
    for pows in mrange([e+1 for p,e in decomp]):
        yield prod(p**e for p,e in zip(P, pows))

def sumdivs(x):
    "Sum of all divisors of x, except x itself (but including 1)"
    return sum(alldivs(x))-x #simple way is better. it does not slows down execution a lot

def sqrti(x):
    "integer square root, equals to floor(sqrt(x)), but can be calculated for long numbers too"
    if x==0:
        return 0
    if x<0:
        raise ValueError("Square root of negative value")
    
    def itr(r):
        return (x//r+r)//2
        
    r=(x+1)//2
    while True:
        r1=itr(itr(r))
        if r1==r:
            break
        r=r1
    #algorithm may give ansver both before x and after x. Choosing one of them.
    if r*r<=x:
        return r
    else:
        return r-1;

        
def issquare(x):
    "checks integer to be exact square"
    q=sqrti(x)
    return x==q*q

def iroot3(x):
    "Integer cubic root of x: biggest integer r, such that r^3 <= x"
    if x==0: return 0
    if x<0:
        return -iroot3(-x)
    r=1
    lower_bound = 1
    upper_bound = x
    i=0
    while True:
        r2=r*r
        r3 = r2*r
        if r3 == x:
            return r #exact solution found
        elif r3 < x:
            lower_bound = max(lower_bound, r)
        else:
            upper_bound = min(upper_bound, r)
        #Update r
        r = (2*r+x//r2)//3
        if r <= lower_bound or r >= upper_bound:
            break
    assert lower_bound < upper_bound
    #now bounds were estimated.
    #use dichotomy to find a better solution
    while upper_bound - lower_bound > 1:
        center = (upper_bound+lower_bound)//2
        fcenter = center ** 3
        if fcenter == x:
            return center
        elif fcenter < x:
            lower_bound = center
        else: 
            upper_bound = center
    return lower_bound

def iscube(x):
    "Returns true, if argument is integer cube"
    r=iroot3(x)
    return x==r**3


def factorial(x):
    "Factorial of x>=0"
    if x==0:
        return 1
    elif x<0:
        raise ValueError( "Factorial defined for x>=0")
    else:
        return prod(range(1,x+1))

def nthperm(l,n):
    "nthperm(l,n) - N-th permutation of list l, 0<=N<len(l)!"
    if len(l)==1:
        return l
    f=factorial(len(l)-1)
    i=n//f
    r=n%f
    return [l[i]]+nthperm(l[:i]+l[i+1:],r)


def digits(a,p=10):
    "representation of number a in positional system, from lowest to highest. for 0, returns []"
    assert(a>=0)
    assert (p>1)
    rval=[]
    while a!=0:
        rval.append(a%p)
        a=a//p
    return rval
    
def from_digits(digs, p=10):
    rval = 0
    a = 1
    for d in digs:
        rval += d*a
        a *= p
    return rval

def memoize(func, dic):
    "Creates memoizing version of function of one argument."
    def memoized(x):
        if x in dic:
            return dic[x]
        else:
            f=func(x)
            dic[x]=f
            return f
    return memoized

def memoized(dic=None):
    """Memoizing decorator"""
    if dic is None:
        dic = dict()
    def decorator(func):
        return memoize(func, dic)
    return decorator

def isperm(a, b, p=10):
    "Checks, whether number a is permutation of number b"
    if p>2:
        q=p-1
        if (a-b)%q:
            return False
    la=digits(a,p)
    la.sort()
    lb=digits(b,p)
    lb.sort()
    return la==lb

    
def phi(x):
    "Euler phi function: number of integers below x, mutually prime with x."
    rval=1
    dprev=1
    for d in pfaci(x):
        if d==dprev:
            rval=rval*d
        else:
            rval=rval*(d-1)
            dprev=d
    return rval
        
    
def gcd(a,b):
    "Greatest common divisor"
    while True:                
        if b==0: return a
        a,b = b,a%b

def lcf(a,b):
    "Least common fract"
    return (a/gcd(a,b))*b

def gcdl(l):
    "Gcd for the list of numbers"
    return reduce(gcd,l)
    
def uniq(lst):
    "Returns unique elements from the SORTED list."
    return [ x for x,_ in grp(lst) ]

def irad(x):
    "Integer radical of x, i.e. the product of the all distinct prime factors of x"
    return prod(uniq(pfaci(x)))

def ispal(x, p=10):
    "Is the number a palindrom"
    if x<0: raise ValueError("Can be applied only to positive numbers")
    powten = 1
    while True:
        pt1=powten*p
        if pt1>x:break
        powten = pt1
    #powten is greatest integer power of 10, less than x
    while True:
        if powten <= 1:
            return True #it is palindron, only 1or 0 digit left
        dh=x/powten #get higher digit
        x=x%powten
        dl=x%p
        x=x/p
        powten/=(p*p)
        if dh != dl:
            return False


def confrac(num, den):
    "numeric continuous fraction"
    c=[]
    while den!=0:
        r = num//den
        c.append(r)
        den,num=num%den,den
    return c

def from_confrac( cf ):
    num, den = 1,0 
    for c in cf[::-1]:
        num, den = den + c*num, num
    return (num, den)


def fibonacci(n, zero=0, one=1):
    "Fast, matrix-power based fibbonacci number calculator"
    M=(one, one, one, zero)
    def mul( m1, m2):
        x11, x12, x21, x22 = m1
        y11, y12, y21, y22 = m2
        return ( x11*y11+x12*y21, x11*y12+x12*y22,
                 x21*y11+x22*y21, x21*y12+x22*y22)
    def mpow(m, n):
        if n < 1: raise ValueError("not supported n<1")
        if n == 1: return m
        mp = mpow(m, n // 2)
        mp2 = mul(mp, mp)
        if n % 2 == 0:
            return mp2
        else:
            return mul(mp2, m)
        
    if n == 0: return 0
    elif n < 0: 
        fp = fibonacci(-n, zero=zero, one=one)
        if n % 2 == 1:
            return fp
        else:
            return -fp
    else:
        mn = mpow(M, n)
        return mn[1]

class ModularInt:
    def __init__(self, x, m):
        self.x = x % m
        self.m = m
    def __str__(self):
        return "%d mod %d"%(self.x, self.m)
    def __repr__(self):
        return "ModularInt(%d,%d)"%(self.x, self.m)

    def __make(self, x):
        return ModularInt(x%self.m, self.m)

    def __get_value(self, y):
        if isinstance(y, ModularInt):
            if y.m != self.m: raise ValueError("Modulos are different")
            return y.x
        else:
            return y

    def divide_both(self, d):
        """Devide both modulo and remainder by some value. Raises exception, if not divisible"""
        if (self.x % d != 0) or (self.m % d != 0):
            raise ValueError("Modular integer is not divisible")
        return ModularInt(self.x//d, self.m//d)
        
    def __mul__(self, y):
        return self.__make( self.x * self.__get_value(y) )

    def __rmul__(self, y):
        return self.__mul__(y)

    def __pos__(self):
        return self
    def __neg__(self):
        return self.__make(-self.x)

    def __add__(self, y):
        return self.__make( self.x + self.__get_value(y) )
    def __radd__(self, y):
        return self.__add__(y)

    def __sub__(self, y):
        return self.__make( self.x - self.__get_value(y) )

    def __pow__(self, n):
        assert( isinstance(n, int))
        if n < 0: raise ValueError("Negative powers not supported yet")
        return self.__make( pow_mod(self.x, n, self.m))
    
    def __eq__(self, y):
        y = self.__get_value(y)
        return (self.x - y) % self.m == 0

def mu(n):
    """Moebius (or Mobius) function mu(n). 
    mu(1) = 1; 
    mu(n) = (-1)^k if n is the product of k different primes; 
    otherwise mu(n) = 0."""
    #oeis: A008683
    
    if n == 1: return 1
    mu_n = 1
    for p, k in grp(pfaci(n)):
        #p^k
        if k != 1: 
            return 0
        else:
            mu_n = -mu_n
    return mu_n

def binomial(n,k):
    """Return binomial coeff (n, i)
    Equal to n!/((n-k)!k!)
    Complexity: O(k), assuming multiplication and divisions are O(1)
    """
    if k < 0 or k > n:
        raise ValueError("K must be not bigger than n")
    k = min(k, n-k)
    c = 1
    for i in range(k):
        c *=  n-i
        c //= i+1 #must be zero remainder
    return c
    
