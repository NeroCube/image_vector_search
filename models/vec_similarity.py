import math
import numpy as np

class VectorSimilarity():

    def __init__(self):
        print('class init')

    def Cosine(self, vec1, vec2) :
        result = self.InnerProduct(vec1,vec2) / (self.VectorSize(vec1) * self.VectorSize(vec2))
        return result

    def VectorSize(self, vec) :
        return math.sqrt(np.sum(np.power(vec, 2)))

    def InnerProduct(self, vec1, vec2) :
        return np.inner(vec1, vec2)

    def Euclidean(self, vec1, vec2) :
        return np.linalg.norm(vec1-vec2)

    def Theta(self, vec1, vec2) :
        return math.acos(self.Cosine(vec1,vec2)) + math.radians(10)

    def Triangle(self, vec1, vec2) :
        theta = math.radians(self.Theta(vec1,vec2))
        return (self.VectorSize(vec1) * self.VectorSize(vec2) * math.sin(theta)) / 2

    def Magnitude_Difference(self, vec1, vec2) :
        return abs(self.VectorSize(vec1) - self.VectorSize(vec2))

    def Sector(self, vec1, vec2) :
        ED = self.Euclidean(vec1, vec2)
        MD = self.Magnitude_Difference(vec1, vec2)
        theta = self.Theta(vec1, vec2)
        return math.pi * math.pow((ED+MD),2) * theta/360

    def TS_SS(self, vec1, vec2) :
        return self.Triangle(vec1, vec2) * self.Sector(vec1, vec2)
