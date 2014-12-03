from libeuler.bwt import bwt
import unittest

class TestBwt(unittest.TestCase):
    def test_banana(self):
        data=list('^BANANA')
        bdata = "".join(bwt(data, eof_char='|'))

        self.assertEqual( bdata,
                          'BNN^AA|A' )
