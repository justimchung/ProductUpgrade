from upgrade_product cimport upgProduct
from cython cimport boundscheck, wraparound
cdef class productQueue:
    """
    This is a minHeap for upgProduct.
    The first element of the queue is an upgProduct with min upgrading cost
    """
    cdef list data
    cdef __push(self, upgProduct p)
    cdef upgProduct __pop(self)
    cpdef int getSize(self)
    cpdef double getMinCost(self)
