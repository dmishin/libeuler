from libeuler import rational
from libeuler.rational import rat as Rational

import unittest
class TestRational(unittest.TestCase):
    def test_construction(self):
        r = Rational(1,1)
        self.assertEqual( r.numden(), (1,1))
        r1 = Rational(2,2)
        self.assertEqual( r1.numden(), (1,1))
        r2 = Rational(2,2,normalize=False)
        self.assertEqual( r2.numden(), (2,2))
        

        r3 = Rational(4,14)
        self.assertEqual( r3.numden(), (2,7))

        r5 = Rational(1)
        self.assertEqual( r5.numden(), (1,1))

        r6 = Rational(7)
        self.assertEqual( r6.numden(), (7,1))

        r7 = Rational(0)
        self.assertEqual( r7.numden(), (0,1))

        
        

    def test_equality(self):
        r0 = Rational( 0, 1)
        r1 = Rational( 1, 1)
        r2 = Rational( 2, 3)
        r3 = Rational( 1, 7)
        self.assertEqual( r0, Rational(0,1) )
        self.assertEqual( r1, Rational(1,1) )
        self.assertEqual( r2, Rational(2,3) )
        self.assertEqual( r3, Rational(1,7) )

        self.assertNotEqual( r0, r1 )
        self.assertNotEqual( r1, r2 )
        self.assertNotEqual( r0, r2 )
        self.assertFalse( r0 != Rational(0,1) )
        self.assertFalse( r1 != Rational(1,1) )

        #Equality to a number
        self.assertEqual( r0, 0 )
        self.assertEqual( r1, 1 )

    def test_unsigned_compatisions(self):
        r0 = Rational( 0, 1)
        r1 = Rational( 1, 1)
        r2 = Rational( 2, 3)
        r3 = Rational( 1, 7)

        self.assertTrue( r0 < r1 )
        self.assertTrue( r0 < r2 )        
        self.assertTrue( r0 < r3 )

        self.assertTrue( r1 > r0 )
        self.assertTrue( r1 > r2 )
        self.assertTrue( r1 > r3 )

        self.assertTrue( r2 > r3 )

        self.assertFalse( r2 > r2 )
        self.assertFalse( r2 < r2 )
        self.assertFalse( r0 > r0 )
        self.assertFalse( r0 < r0 )

        #COmparisions with a number
        self.assertTrue( r1 > 0 )
        self.assertTrue( r2 < 1 )

        self.assertTrue( r0 >= 0)
        self.assertTrue( r0 <= 0)

        self.assertTrue( r0 <= 1)
        self.assertFalse( r0 >= 1)

        self.assertTrue( r1 >= 0)
        self.assertFalse( r1 <= 0)

        self.assertTrue( r2 > 0)
        self.assertTrue( r2 >= 0)
        self.assertTrue( r2 < 1)
        self.assertTrue( r3 < 1)

    def test_signed_comparisions(self):
        r1 = Rational(2,3)
        r2 = Rational(-2, 3)

        self.assertTrue( r1 > r2 )
        self.assertTrue( r2 < r1 )
        self.assertTrue( r2 != r1 )
        self.assertTrue( r2 < 0 )

    def test_arithmetics(self):
        
        R = Rational
        ae = self.assertEqual

        #Summation
        ae( R(1,2) + R(1,2),  R(1,1))
        ae( R(1,2) + R(1,3),  R(5,6))
        ae( R(2,3) + R(4,3),  R(2,1))
        ae( R(1,2) + 1, R(3,2))
        ae( 1 + R(1,2), R(3,2))

        #Unaries
        ae( +R(2,3),  R(2,3))
        ae( -R(2,3),  R(-2,3))
        ae( -R(0), R(0) )
        ae( 0*R(-2,3), 0*R(4,5) )

        #Subtraction
        ae( R(3,2) - R(2,3),  R(5,6) )
        ae( R(1,2) - R(1,2),  R(0,1) )
        ae( R(1,2) - R(2,3),  -R(1,6) )
        ae( R(1,2) - 1, -R(1,2))
        ae( 1 - R(2,3), R(1,3))

        #Multiplication
        ae( R(3,2) * R(2,3),  1 )
        ae( R(3,2) * R(2,7),  R(3,7) )
        ae( R(3,2) * 3, R(9,2))
        ae( R(5,7) * 7, 5 )

        #Division
        ae( R(3,2) / R(3,2),  1 )
        ae( R(3,2) / R(3,7),  R(7,2) )
        ae( 1 / R(2), R(1,2))
        ae( R(3) / 7, R(3,7))


        #Power
        ae( R(2,3) ** 2, R(4,9))
        ae( R(2,3) ** 0, 1)
        ae( R(2,3) ** (-1), R(3,2))

        #Abs value
        ae( abs(R(2,3)), R(2,3))
        ae( abs(R(-2,3)), R(2,3))
        
    def test_intpart_fracpart(self):
        r = Rational(7,5)
        self.assertEqual(r.intpart(), 1)
        self.assertEqual(r.fracpart(), Rational(2,5))
        
        r1 = Rational(-7,5)
        self.assertEqual(r1.intpart(), -2)
        self.assertEqual(r1.fracpart(), Rational(3,5))
        
    def test_copy(self):
        r = Rational(7,5)
        r1 = r.copy()
        self.assertEqual(r, r1)
        r.num = 8
        self.assertNotEqual(r, r1)
        
    def test_is_zero(self):
        R = Rational
        self.assertTrue( Rational(0).iszero() )
        self.assertTrue( Rational(0,1).iszero() )
        self.assertTrue( Rational(0,5, False).iszero() )

        self.assertFalse( Rational(1).iszero() )
        self.assertFalse( Rational(1,1).iszero() )

