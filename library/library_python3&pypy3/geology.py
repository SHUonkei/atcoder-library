#d度反時計回りに回転する
def rot(x,y,d):
    import math
    d = math.radians(d)
    return [(x*math.cos(d) - y*math.sin(d)),(y*math.cos(d)+x*math.sin(d))]
