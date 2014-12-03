from libeuler.spacefill.hilbert import d2xy, xy2d
from libeuler.spacefill.hilbert_np import hilbert_indices
import  unittest
from numpy import array
import numpy as np


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

            
class TestHilbertIndex(unittest.TestCase):
    def test_hilbert_indices0(self):
        m = hilbert_indices(0)
        me = array( [[0]], dtype=np.int )        
        self.assertEqual( m, me )
    def test_hilbert_indices1(self):
        m = hilbert_indices(1)
        me = array( [[0,3],
                     [1,2]], 
                    dtype=np.int )        
        self.assertTrue( (m == me).all() ) 
        
    def test_hilbert_indices2(self):
        m = hilbert_indices(2)
        me = array( [[0,1,14,15],
                     [3,2,13,12],
                     [4,7,8,11],
                     [5,6,9,10]], 
                    dtype=np.int )        
        self.assertTrue( (m == me).all(), "returned: \n{m}, expected: \n{me}".format(m=m,me=me) ) 

    def test_hilbert_indicesN(self):
        N = 6
        m = hilbert_indices(N)
        x,y = 0,0
        for i in range(4**N-1):
            self.assertEqual( m[x,y], i, "m[{x},{y}]=={i}".format(**locals()))
            
            found = False
            for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                x1 = x+dx
                y1 = y+dy
                if x1 < 0 or x1 >= 2**N: continue
                if y1 < 0 or y1 >= 2**N: continue
                if m[x1,y1] == i+1:
                    found = True
                    break
            self.assertTrue(found, "not found neighbor {i} for {x}, {y}".format(**locals()))
            x,y = x1,y1
            
        
            
