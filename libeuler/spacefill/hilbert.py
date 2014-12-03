from __future__ import division, print_function
#generate points on hilbert curve
#convert (x,y) to d
#code from Wikipedia
def xy2d (n, x, y):
    d=0
    s=n//2
    while s>0:
        rx = (x & s) > 0
        ry = (y & s) > 0
        d += s * s * ((3 * rx) ^ ry)
        x,y = rot(s, x, y, rx, ry)
        s//=2
    return d


 
#convert d to (x,y)
def d2xy(n, d) :
    t=d
    x = y = 0
    s = 1
    while s<n:
        rx = 1 & (t//2)
        ry = 1 & (t ^ rx)
        x, y = rot(s, x, y, rx, ry)
        x += s * rx
        y += s * ry
        t //= 4
        s *=2
    return x,y
    

 
#rotate/flip a quadrant appropriately
def rot( n,  x,  y,  rx,  ry) :
    if ry == 0 :
        if (rx == 1) :
            x = n-1 - x
            y = n-1 - y
        return y, x
    else:
        return x, y
    
    

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
