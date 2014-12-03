#copipe from rle2svg
def parse(rle_string):
    """ Decode the RLE string, generating sequence of the x,y pairs
    Based on the CoffeScript code"""
    x = 0
    y = 0
    curCount = 0
    for i in range(0, len(rle_string)):
        c = rle_string[i]
        if "0" <= c and c <= "9":
            curCount = curCount * 10 + int(c)
        else:
            count = max(curCount, 1)
            curCount = 0
            if c == "b":
                x += count
            elif c == "$":
                y += count
                x = 0
            elif c == "o":
                for j in range(0,count):
                    yield (x, y)
                    x+=1
            else:
                raise ValueError( "Unexpected character '%s' at position %d"%(c, i))

def rle2cells(rle, dx=0, dy=0):
    """Return list of cells for the given rle"""
    return [ (x+x0,y+y0) for x,y in parse(rle) ]
