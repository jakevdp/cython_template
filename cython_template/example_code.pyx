def example_function(int N):
    """Example cython function"""
    cdef int count = 0
    for i in range(N):
        count += i
    return count
