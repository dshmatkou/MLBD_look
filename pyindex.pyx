from libcpp.string cimport string
from libcpp.vector cimport vector


cdef extern from "index/index.h":
    cdef cppclass SmallWorldIndex:
        SmallWorldIndex() except +
        SmallWorldIndex(int, int) except +
        int GetDim()
        int AddItem(string&, vector[float]&)
        void FindKNearest(int&, vector[float]&, vector[int]&)
        void GetKeyValue(int&, string&, vector[float]&)



cdef class PySmallWorldIndex:
    cdef SmallWorldIndex c_index

    def __cinit__(self, int dim, int connectivity):
        self.c_index = SmallWorldIndex(dim, connectivity)

    @property
    def dimension(self):
        return self.c_index.GetDim()

    def add_item(self, key, embedding):
        assert len(embedding) == self.dimension

        cdef string c_key = key.encode()
        cdef vector[float] c_embedding = embedding
        result = self.c_index.AddItem(c_key, c_embedding)
        if result:
            raise RuntimeError('Error while add new item')

    def find_k_nearest(self, k, embedding):
        assert k > 0
        assert len(embedding) == self.dimension

        cdef vector[float] c_embedding = embedding
        cdef vector[int] c_result

        self.c_index.FindKNearest(k, c_embedding, c_result)

        result = []
        cdef string out_c_key
        cdef vector[float] out_c_embedding
        for item in c_result:
            out_c_key.clear()
            out_c_embedding.clear()
            self.c_index.GetKeyValue(item, out_c_key, out_c_embedding)
            result.append(
                (out_c_key.decode(), tuple(out_c_embedding))
            )

        return result


# delete it, just to save backwards compatibility
def pysum(a, b):
    return a + b
