from unittest import TestCase

from libeuler.ca import rle

class TestRle(TestCase):
    def test_parse(self):
        self.assertEqual( list(rle.parse( "" )), [] )
        self.assertEqual( list(rle.parse( "$" )), [] )
        self.assertEqual( list(rle.parse( "b" )), [] )
        self.assertEqual( list(rle.parse( "o" )), [(0,0)] )
        self.assertEqual( list(rle.parse( "bo" )), [(1,0)] )
        self.assertEqual( list(rle.parse( "$o" )), [(0,1)] )
        self.assertEqual( list(rle.parse( "2o" )), [(0,0),(1,0)] )
        self.assertEqual( list(rle.parse( "12o" )),
                        [(i,0)for i in range(12)] )
        
        self.assertRaises( lambda: list(rle.parse( "asd" )) )
