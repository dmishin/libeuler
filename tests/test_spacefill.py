from libeuler.spacefill.hilbert import d2xy, xy2d
import  unittest

class TestHilb(unittest.TestCase):
    def test_d2xy(self):
        xys = set()
        for d in range(64):
            xy = d2xy(8, d)
            xys.add(xy)
        xys_expected = set()
        for x in range(8):
            for y in range(8):
                xys_expected.add((x,y))
        self.assertEqual(len(xys), 64)
        self.assertEqual(xys, xys_expected)
        
    def test_xy2d(self):
        for d in range(64):
            x,y = d2xy(8, d)
            d1 = xy2d(8,x,y)
            self.assertEqual(d1, d, "d2xy(8,{d})=({x},{y}), xy2d(8,{x},{y})={d1}".format(**locals()))
