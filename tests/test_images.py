from libeuler.images import value_diapason
import unittest
import numpy as np

class TestValueDiapason(unittest.TestCase):
    def test_value_diapason_zeros(self):
        data = np.zeros( (100, 100) )
        low, high = value_diapason( data )
        
        self.assertLessEqual( low, high )
        self.assertLessEqual( low, 0 )
        self.assertLessEqual( 0, high )

    def test_value_diapason_ones(self):
        data = np.ones( (100, 100) )
        low, high = value_diapason( data )
        
        self.assertLessEqual( low, high )
        self.assertLessEqual( low, 1 )
        self.assertLessEqual( 1, high )

    def test_value_diapason_point_noise(self):
        data = np.zeros( (100, 100) )
        data[ 10, 20] = 100
        data[ 5, 70] = -10
        
        low, high = value_diapason( data )
        
        self.assertLessEqual( low, high )
        self.assertLessEqual( low, 0 )
        self.assertLessEqual( 0, high )

        #check that -10 and 100 are not in the diapason
        self.assertLessEqual( -10, low )
        self.assertLessEqual( high, 100 )

    def test_value_diapason_range(self):
        data = np.linspace( 0, 10, 10000 )
        low, high = value_diapason( data )

        self.assertLessEqual( low, high )
        self.assertLessEqual( 0, low )
        self.assertLessEqual( high, 10 )

        self.assertLessEqual( low, 1 )
        self.assertLessEqual( 9, high )
