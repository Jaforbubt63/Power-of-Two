import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        
        m = math.log2(n)
        ceil_m = int(math.ceil(m))
        floor_m = int(math.floor(m))
        return ceil_m == floor_m
        