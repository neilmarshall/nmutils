from cpython.object cimport Py_EQ, Py_NE, Py_LE, Py_LT, Py_GE, Py_GT

cdef class Triple():
    """Class that holds a Pythagorean triple,  allowing comparison of triples by perimeter"""
    cdef readonly int a, b, c

    def __init__(self, _a, _b, _c):
        self.a = _a
        self.b = _b
        self.c = _c

    def __richcmp__(x, y, int op):
        cdef int xval, yval
        xval = x.a + x.b + x.c
        yval = y.a + y.b + y.c
        if op == Py_EQ:
            return xval == yval
        elif op == Py_NE:
            return xval != yval
        elif op == Py_LE:
            return xval <= yval
        elif op == Py_LT:
            return xval < yval
        elif op == Py_GE:
            return xval >= yval
        elif op == Py_GT:
            return xval > yval
        else:
            assert False

