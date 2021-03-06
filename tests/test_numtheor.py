import libeuler.numtheor as nt
import itertools
import unittest

class TestPolygonal(unittest.TestCase):
    def test_polygonal(self):
        def polylist(p, n): 
            return [nt.polygonal(p,i) 
                    for i in range(1, n+1) ]
             
        self.assertEqual( polylist(3, 5),
                          [1, 3, 6, 10, 15] )
        self.assertEqual( polylist(4, 5),
                          [1, 4, 9, 16, 25] )

        self.assertEqual( polylist(5, 5), #,n=n(3n−1)/2
                          [1, 5, 12, 22, 35] )
        self.assertEqual( polylist(6, 5), #,n=n(2n−1)
                          [1, 6, 15, 28, 45] )
        self.assertEqual( polylist(7, 5), #,n=n(5n−3)/2
                          [1, 7, 18, 34, 55] )
        self.assertEqual( polylist(8, 5), #,n=n(3n−2)
                          [1, 8, 21, 40, 65] )

        def test_invpolygonal(self):
            for p in range(3, 10):
                for n in range(1, 10):
                    pn = polygonal(p,n)
                    n1 = ipolygonal(p, pn)
                    self.assertEqual( n1, n, 
                                      "invpolygonal({p},polygonal({p}, {n})) = {n1} != {n}".format(p=p, n=n,n1=n1))

class TestRoots(unittest.TestCase):
    def test_sqrti(self):
        eq = self.assertEqual
        eq( nt.sqrti(0), 0 )
        eq( nt.sqrti(2), 1 )
        eq( nt.sqrti(3), 1 )
        eq( nt.sqrti(4), 2 )
        eq( nt.sqrti(5), 2 )
        eq( nt.sqrti(15), 3 )
        x = 111111111111111111111
        eq( nt.sqrti(x**2 + 1000), x )
        eq( nt.sqrti(x**2 - 1000), x-1 )
    def test_issquare(self):
        self.assertTrue( nt.issquare( 0 ) )
        self.assertTrue( nt.issquare( 1 ) )
        self.assertTrue( nt.issquare( 25 ) )
        self.assertTrue( nt.issquare( 111111111111111111111**2 ) )

        self.assertFalse( nt.issquare( 2 ) )
        self.assertFalse( nt.issquare( 3 ) )
        self.assertFalse( nt.issquare( 28 ) )
        self.assertFalse( nt.issquare( 1 + 111111111111111111111**2 ) )

    def test_iroot3(self):
        eq = self.assertEqual
        eq( nt.iroot3(0), 0 )
        eq( nt.iroot3(1), 1 )
        eq( nt.iroot3(2), 1 )
        eq( nt.iroot3(3), 1 )
        eq( nt.iroot3(7), 1 )
        eq( nt.iroot3(8), 2 )
        eq( nt.iroot3(9), 2 )

        eq( nt.iroot3(26), 2  )
        eq( nt.iroot3(27), 3  )
        eq( nt.iroot3(28), 3  )

        x = 111111111111111111111111111
        eq( nt.iroot3(x**3), x  )
        eq( nt.iroot3(x**3 + 1000), x  )
        eq( nt.iroot3(x**3 - 1000), x-1  )
        
        
class TestLists(unittest.TestCase):
    def test_nthperm(self):
        sample = [1,2,3,4,5] # 5! = 120
        permutations = list(itertools.permutations(sample))
        permutations.sort() #sort lexicographically
        for i, perm in enumerate(permutations):
            self.assertListEqual( nt.nthperm(sample, i), list(perm) )
    def test_nthperm_0(self):
        self.assertListEqual( nt.nthperm( [1], 0 ), [1] )
        self.assertListEqual( nt.nthperm( [1,2], 0 ), [1,2] )
        self.assertListEqual( nt.nthperm( [1,2,3,4,5,6,7,8], 0 ), [1,2,3,4,5,6,7,8] )

    def test_nthperm_last(self):
        self.assertListEqual( nt.nthperm( [1,2], 1 ), [2,1] )
        self.assertListEqual( nt.nthperm( [1,2,3,4,5,6,7,8], nt.factorial(8)-1 ), [8,7,6,5,4,3,2,1] )


    def test_grp(self):
        eq = self.assertEqual
        grp = lambda l: list(nt.grp(l))
        eq( grp( [] ), [] )
        eq( grp( [1] ), [(1,1)] )
        eq( grp( [1,2,3] ), [(1,1),(2,1),(3,1)] )
        eq( grp( [1,1,3] ), [(1,2),(3,1)] )        
        eq( grp(nt.pfac(128*81*121)), [(2,7),(3,4),(11,2)] )
    def test_findfirst(self):
        eq = self.assertEqual
        lst = [1,2,3,4,5,6,7,8,9]
        eq( nt.findfirst(lst, lambda x: x>0), 1)
        eq( nt.findfirst(lst, lambda x: x==9), 9)
        eq( nt.findfirst(lst, lambda x: x>5), 6)
        eq( nt.findfirst(lst, lambda x: x>100), None)
    def test_zip_with_previous(self):
        lzipp = lambda s: list(nt.zip_with_previous(s))
        self.assertListEqual( lzipp([1,2,3]), [(1,2),(2,3)] )
        self.assertListEqual( lzipp([1,2]), [(1,2)] )
        self.assertListEqual( lzipp([1]), [] )
        self.assertListEqual( lzipp([]), [] )
class TestFib(unittest.TestCase):
    def test_fibonacci(self):
        eq = self.assertEqual

        fibs = [0,1,1,2,3,5,8,13]
        for i, fi in enumerate(fibs):
            eq( nt.fibonacci(i), fi, "Check bibonacci(%d)"%i)
        #Check far away fibonacci
        n = 2000
        fn = nt.fibonacci(n)
        fn1 = nt.fibonacci(n+1)
        fn2 = nt.fibonacci(n+2)
        eq( fn+fn1, fn2, "Check fibonacci equality for n = 2000" )
        self.assertTrue( fn1 > fn )
    def test_negativefib(self):
        #  -3 -2   -1 0  1
        #  -2, 1, -1, 0, 1
        
        for n in range(-20, 10):
            self.assertEqual( nt.fibonacci(n)+nt.fibonacci(n+1), 
                              nt.fibonacci(n+2),
                              "Test f(%d)+f(%d)=f(%d)"%(n,n+1, n+2) )
class TestConfrac(unittest.TestCase):
    def test_confrac(self):
        eq = self.assertSequenceEqual
        eq( nt.confrac( 1, 1 ), [1] )
        eq( nt.confrac( 2, 1) , [2] )
        eq( nt.confrac( 1, 2) , [0, 2] )
        eq( nt.confrac( 5, 7) , [0, 1, 2, 2] )
        
    def test_from_confrac(self):
        eq = self.assertEqual
        eq( nt.from_confrac( [1] ), ( 1, 1 ) )
        eq( nt.from_confrac ( [2] ), ( 2, 1) )
        eq( nt.from_confrac ( [0, 2] ), ( 1, 2) )
        eq( nt.from_confrac ( [0, 1, 2, 2] ), ( 5, 7) )

        #Composite test
        eq( nt.from_confrac( nt.confrac(317, 997)), (317, 997))

class TestModularInt(unittest.TestCase):    
    def test_basic(self):
        z = nt.ModularInt(0, 5)
        e = nt.ModularInt(1, 5)
        
        at = self.assertTrue
        at( z == z )
        at( e == e )
        at( e != z )
        at( z != e )

        at( z == nt.ModularInt(0, 5) )
        at( e == nt.ModularInt(1, 5) )
    def test_arithmetics(self):
        z = nt.ModularInt(0, 5)
        e = nt.ModularInt(1, 5)        
        e2 = nt.ModularInt(2, 5)
        
        ae = self.assertEqual

        ae( z+z, z, "Sum with zero" )
        ae( z+e, e, "Sum with zero" )
        ae( e+z, e, "Sum with zero" )
        ae( e2+z, e2, "Sum with zero" )
        
        ae( e+e, e2, "1+1=2" )
        ae( e2+e2+e, z, "2+2+1=0 mod 5" )
        
        
        ae( +z, z, "Unary +")
        ae( +e, e, "Unary +")
        ae( -z, z, "Unary -")
        ae( -e+e, z, "-1+1=0")
        ae( -e+e2, e, "-1+2=1")
        ae( -(-e2), e2)

        ae( e-e, z, "Minus" )
        ae( e2-e, e )
        ae( e2-e2, z )
        ae( -e2-e2, e )
    def test_divboth(self):
        a = nt.ModularInt(6,14)
        self.assertEqual( a.divide_both(1), a)
        self.assertEqual( a.divide_both(2), nt.ModularInt(3,7))

        with self.assertRaises( ValueError):
            b = a.divide_both( 3 )
            
        
class TestMrange(unittest.TestCase):
    def test_1_arg(self):
        eq = self.assertEqual
        def mr1(ends):
            return list(nt.mrange(ends))
        
        eq( mr1([1]), [(0,)] )
        eq( mr1([2]), [(0,), (1,)] )
        eq( mr1([3]), [(0,), (1,), (2,)] )

        eq( mr1([1,1]), [(0,0)] )
        eq( mr1([2,2]), [(0,0), (1,0), (0,1), (1,1)] )
    def test_2_arg(self):

        r2_32 = [(0,0), (1,0), (2,0),
                 (0,1), (1,1), (2,1) ]

        self.assertListEqual( list(nt.mrange( (3,2) )),
                              r2_32 )

        self.assertListEqual( list(nt.mrange( (0,0), (3,2) )),
                              r2_32 )

        self.assertListEqual( list(nt.mrange( (0,0), (3,2), (1,1) )),
                              r2_32 )

    def test_3_arg(self):

        def rng3():
            for i in range(3):
                for j in range(4):
                    for k in range(5):
                        yield (k,j,i)

        for expected, got in zip(rng3(),
                                 nt.mrange( (5,4,3))):
            self.assertEqual( expected, got )


class TestDivisors(unittest.TestCase):
    def test_numdivs(self):
        eq = self.assertEqual
        eq( nt.numdivs(1), 1 )
        eq( nt.numdivs(2), 2 )
        eq( nt.numdivs(3), 2 )

        def naive_numdivs(x):
            return len([i for i in range(1, x+1) 
                        if x % i == 0])

        eq( nt.numdivs(6), naive_numdivs(6))
        for x in range(7,100):
            eq( nt.numdivs(x), naive_numdivs(x))
    def test_alldivs(self):
        eq = self.assertSetEqual
        eq( set(nt.alldivs(1)), set([1]))
        eq( set(nt.alldivs(2)), set([1,2]))
        eq( set(nt.alldivs(6)), set([1,2,3,6]))
        eq( set(nt.alldivs(16)), set([1,2,4,8,16]))
        

    def test_sumdivs(self):
        "Sum of all divisors of x, except x itself (but including 1)"
        eq = self.assertEqual
        eq( nt.sumdivs(1), 0)
        eq( nt.sumdivs(2), 1)
        eq( nt.sumdivs(6), 6)
    def test_prod(self):
        eq = self.assertEqual
        eq( nt.prod( [] ), 1 )
        eq( nt.prod( [1] ), 1 )
        eq( nt.prod( [1,2,3,4] ), 1*2*3*4 )

        eq( nt.prod( [1,2,3,4], initial=10),
            10*1*2*3*4 )

    def test_gcd(self):
        eq = self.assertEqual
        eq( nt.gcd(1, 1), 1)
        eq( nt.gcd(1, 5), 1)
        eq( nt.gcd(5, 1), 1)

        eq( nt.gcd(5, 5), 5)
        eq( nt.gcd(6, 15), 3)
        eq( nt.gcd(15, 6), 3)
        eq( nt.gcd(16, 16), 16)
        eq( nt.gcd(16, 15), 1)
        eq( nt.gcd(2**20, 3**10), 1)
        eq( nt.gcd(2**20, 3**10), 1)
    def test_lcf(self):
        eq = self.assertEqual
        eq( nt.lcf(1,1), 1)
        eq( nt.lcf(1,5), 5)
        eq( nt.lcf(5,1), 5)
        eq( nt.lcf(5,5), 5)

        eq( nt.lcf(15, 6), 2*3*5)
        eq( nt.lcf(2**20, 3**10), 2**20*3**10)

class TestDigits(unittest.TestCase):
    def test_digits(self):
        eq = self.assertSequenceEqual
        eq( nt.digits(0, 10), [] )
        eq( nt.digits(1, 10), [1] )
        eq( nt.digits(12345, 10), [5,4,3,2,1] )

        eq( nt.digits(8, 2), [0,0,0,1] )
        eq( nt.digits(7, 2), [1,1,1] )
    def test_from_digits(self):
        eq = self.assertEqual
        eq( nt.from_digits( [1,2,3], 10 ), 321 )
        eq( nt.from_digits( [1,1,1], 2 ), 7 )
        eq( nt.from_digits( [], 2 ), 0 )
    def test_isperm(self):
        et = self.assertTrue
        #Decimal
        et( nt.isperm( 123, 123, 10 ) )
        et( nt.isperm( 123, 321, 10 ) )
        et( nt.isperm( 123, 213, 10 ) )
        et( nt.isperm( 5, 5, 10 ) )
        et( nt.isperm( 11511, 51111, 10 ) )

        et( not nt.isperm( 12, 23, 10 ) )
        et( not nt.isperm( 12, 112, 10 ) )
        et( not nt.isperm( 12, 1, 10 ) )
        et( not nt.isperm( 1111, 1, 10 ) )
        #Defautl is decimal
        et( nt.isperm( 123, 321 ) )
        et( not nt.isperm( 123, 521 ) )
        #Base-2
        et( nt.isperm( 3, 3, 2 ) ) #11
        et( nt.isperm( 5, 6, 2 ) ) #101, 110
        et( not nt.isperm( 7, 8, 2 ) ) #111, 1000
        et( not nt.isperm( 5, 4, 2 ) ) #101, 100

class TestPrimes(unittest.TestCase):
    def setUp(self):
        pass

    def test_squarefree(self):
        squarefrees = [2,3,5,6,7,10,11,13,14,15,17,19,21]
        nonsqfrees =  [4,8,9,12,16,18,20,24,25,27,28]
        for x in squarefrees:
            self.assertTrue( nt.squarefree(x), "%d must be squarefree"%(x) )
        for x in nonsqfrees:
            self.assertFalse( nt.squarefree(x), "%d must not be squarefree"%(x))

    def test_is_prime(self):        
        eq = self.assertEqual
        et = self.assertTrue

        et( nt.isprime( 2 ) )
        et( nt.isprime( 3 ) )
        et( nt.isprime( 5 ) )
        et( nt.isprime( 7919 ) )

        et( not nt.isprime( 0 ) )
        et( not nt.isprime( 1 ) )
        et( not nt.isprime( 4 ) )
        et( not nt.isprime( 6 ) )
        et( not nt.isprime( 15 ) )
        et( not nt.isprime( 7919**2 ) )

    def test_primes_gen(self):
        prs = [2,3,5,7,11,13,17,19,23]
        for p1, p2 in zip(prs, nt.primes_gen()):
            self.assertEqual(p1, p2)

    def test_primes_gen_table(self):

        for i, (p1, p2) in enumerate(zip(nt.primes_gen(),
                                         nt.primes_gen_table())):
            if i == 100: break
            self.assertEqual(p1, p2)

    def test_primes(self):
        """Test seive"""
        prs = nt.primes(1000)
        self.assertEqual( prs[-1], 997 )
        self.assertEqual( prs[0], 2)
        
        prs_set = set(prs)

        for x in range(1000+1):
            if x in prs_set:
                self.assertTrue( nt.isprime(x))
            else:
                self.assertTrue( not nt.isprime(x))
                
    def test_pfac(self):
        ae = self.assertEqual
        ae( nt.pfac(1), [] )
        ae( nt.pfac(2), [2] )
        ae( nt.pfac(3), [3] )
        ae( nt.pfac( 997 ), [997] )
        ae( nt.pfac(2**16), [2]*16 )
        ae( nt.pfac(17**3), [17]*3 )
        ae( nt.pfac(6), [2,3])
 
    def test_pfac_table(self):
        ae = self.assertListEqual
        table = nt.primes( 100 )
        
        ae( list(nt.pfac_table(1, table)), [] )
        ae( list(nt.pfac_table(2, table)), [2] )
        ae( list(nt.pfac_table(3, table)), [3] )
        ae( list(nt.pfac_table( 997, table )), [997] )
        ae( list(nt.pfac_table(2**16, table)), [2]*16 )
        ae( list(nt.pfac_table(17**3, table)), [17]*3 )
        ae( list(nt.pfac_table(6, table)), [2,3])
       
    def test_phi(self):
        ae = self.assertEqual
        def phi_naive(x):
            n = 0
            for i in range(1,x+1):
                if nt.gcd(i, x)==1:
                    n += 1
            return n
        for x in range(1, 100):
            ae(nt.phi(x), phi_naive(x), "Checking phi for x=%d"%(x))

    def test_mu(self):
        expected = [1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0, -1, 1, 1, 0, -1, 0, -1, 0, 1, 1, -1, 0, 0, 1, 
                    0, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1, 1, 1, 0, -1, -1, -1, 0, 0, 1, -1, 0, 0, 0, 1, 0, 
                    -1, 0, 1, 0, 1, 1, -1, 0, -1, 1, 0, 0, 1, -1, -1, 0, 1, -1, -1, 0, -1, 1, 0, 0, 1]

        a8683 = nt.mu

        for i, ai in enumerate(expected):
            ai_c = a8683(i+1)
            self.assertEqual( ai, ai_c, "For mu(%d), expected %d, but got %d"%(i+1, ai, ai_c) )
    def test_arder(self):
        expected = [0, 0, 1, 1, 4, 1, 5, 1, 12, 6, 7, 1, 16, 1, 9, 8, 32, 1, 21, 1, 24, 10, 13, 1, 44, 10, 15, 27, 32, 1, 31, 1, 80, 14, 19, 12, 60, 1, 21, 16, 68, 1, 41, 1, 48, 39, 25, 1, 112, 14, 45, 20, 56, 1, 81, 16, 92, 22, 31, 1, 92, 1, 33, 51, 192, 18, 61, 1, 72, 26, 59, 1, 156, 1, 39, 55, 80, 18, 71]

        a003415 = nt.arder
        for i, ai in enumerate(expected):
            ai_c = a003415(i)
            self.assertEqual( ai, ai_c, "For arithmetic derivative %d': expeced %d, but gut %d"%(i, ai, ai_c))


class TestBinomial(unittest.TestCase):
    def test_simple(self):
        expected = [ [1],
                     [1,1],
                     [1,2,1],
                     [1,3,3,1],
                     [1,4,6,4,1],
                     [1,5,10,10,5,1]]
        for n, row in enumerate( expected):
            for k, cnk in enumerate(row):
                cnk_got = nt.binomial(n,k)
                self.assertEqual( cnk,
                                  cnk_got,
                                  "C(%d, %d): expected %d, got %d"%(n,k,cnk, cnk_got))
    def test_large(self):

        for n, k in ((1000,500),
                     (2000,30),
                     (100, 41),
                     (111,37)):
            self.assertEqual( nt.binomial(n,k),
                              nt.binomial(n-1,k)+nt.binomial(n-1,k-1),
                              "C(%d,%d) != C(%d,%d)+C(%d,%d)"%(n,k,n-1,k-1,n-1,k))

    def test_factorial_formula(self):
        fac = nt.factorial
        for n in range(10):
            for k in range(n+1):
                self.assertEqual( nt.binomial(n,k),
                                  fac(n) / (fac(n-k)*fac(k)),
                                  "C({n},{k})={n}!/(({n}-{k})!{k}!)".format(n=n,k=k))

if __name__=="__main__":
    unittest.main()

