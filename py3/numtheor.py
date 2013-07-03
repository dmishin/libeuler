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
    for p in range(3,int(sqrti(x))+1,2):
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
    return [p for p in range(n) if seive[p]]




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
            x=x/p
            yield p


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

def numdivs(n):
    "number of divisors"
    if n==1: return 1
    return prod([f[1]+1 for f in grp(pfac(n))])

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
    "Multidimensional range"
    if steps==None:
        steps=(1,)*len(begins)
    if ends==None:
        ends=begins
        begins=(0,)*len(ends)
        
    if len(begins)!=len(ends) or len(ends)!=len(steps):
        raise Exception
    bes=list(zip(begins,ends,steps))
    
    def mrange_rec(bes):
        if len(bes)==0:
            return
        if len(bes)==1:
            for x in range(*(bes[0])):
                yield (x,)
        for x2_xn in mrange_rec(bes[1:]):
            for x1 in range(*(bes[0])):
                yield (x1,)+x2_xn
    for x in mrange_rec(bes):
        yield x
                

def prod(l):
    "Product of all items in list"
    p = 1
    for x in l:
        p *= x
    return p

def alldivs(x):
    "generates all divisors of x, including 1 and the number itself"
    if x == 1:
        yield 1
        return

    decomp=tuple(grp(pfac(x)))    
    #enumerate all powers
    P=[p for p,e in decomp]
    
    for pows in mrange([p_e[1]+1 for p_e in decomp]):
        yield prod([p**e for p,e in zip(P, pows) ])

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
    "Integer cubic root of x"
    if x<0:
        return -iroot3(-x)
    r=1
    def itr(r):
        r2=r*r
        return (2*r2*r+x)/(3*r2)
    while True:
        r0,r=r,itr(itr(r))
        if r0==r:
            break
    #algorithm may give ansver both before x and after x. Choosing one of them.
    if r**3<=x:
        return r
    else:
        return r-1;

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
    i=n/f
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
        if a%b==0: return b
        a,b = b,a%b

def lcf(a,b):
    "Least common fract"
    return (a/gcd(a,b))*b

def gcdl(l):
    "Gcd for the list of numbers"
    return reduce(gcd,l)
    
def uniq(lst):
    "Returns unique elements from the SORTED list."
    if len(lst)==0:
        return []
    x0 = lst[0]
    rlist = [x0]
    for x in lst[1:]:
        if x!=x0:
            rlist.append(x)
            x0=x
    return rlist


def irad(x):
    "Integer radical of x, i.e. the product of the all distinct prime factors of x"
    return prod(uniq(pfac(x)))

def ispal(x, p=10):
    "Is the number palindrom"
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
    M=[one, one, one, zero]
    def mul( m1, m2):
        x11, x12, x21, x22 = m1
        y11, y12, y21, y22 = m2
        return [ x11*y11+x12*y21, x11*y12+x12*y22,
                 x21*y11+x22*y21, x21*y12+x22*y22]
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
        assert (self.x % d == 0)
        assert (self.m % d == 0)
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
        if n == 0:
            return self.__make(1)
        if n == 1:
            return self
        x1 = self ** (n//2)
        x1 = x1*x1
        if n%2 == 0:
            return x1
        else:
            return x1 * self
    
