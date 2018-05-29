class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        ref = {}
        for i in range(len(A)):
            s = B - A[i]
            if ref.get(str(s)):
                return ref.get(str(s)) + 1, i + 1
            elif not ref.get(str(s)) and not ref.get(str(A[i])):
                ref[str(A[i])] = i
        return []
            
