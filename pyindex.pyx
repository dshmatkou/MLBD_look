

cdef extern from "index/index.h":
    cdef int cppsum(int x, int y);


def pysum(x, y):
    cdef int xx = int(x)
    cdef int yy = int(y)
    return int(cppsum(xx, yy))

def pyhandle(data):
    return data