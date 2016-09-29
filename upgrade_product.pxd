cdef class upgProduct:
    """
    The upgraded product class. The class is used in the upgrade algorithm.
    self.attributes is the attribute list of the product
    self.getUpgCost returns the upgrade cost of the product
    """
    cdef public int[::1] attributes
    cdef double upgCost
    cdef inline __setCost(self, double aCost)
    cdef inline double __getCost(self)
