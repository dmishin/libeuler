import numtheor as nt
import unittest
class TestRoots(unittest.TestCase):
    def test_sqrti(self):
        eq = self.assertEqual
        eq( nt.sqrti(2), 1 )
        eq( nt.sqrti(3), 1 )
        eq( nt.sqrti(4), 2 )
        eq( nt.sqrti(5), 2 )
        eq( nt.sqrti(15), 3 )
    def test_issquare(self):
        pass
    def test_iroot3(self):
        pass

class TestLists(unittest.TestCase):
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
        eq = self.assertEqual
        def mr1(ends):
            return list(nt.mrange(ends))

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

class TestPrimes(unittest.TestCase):
    def setUp(self):
        pass
    
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

if __name__=="__main__":
    unittest.main()

