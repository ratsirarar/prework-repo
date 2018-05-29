class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        res = [0]*len(A)
        a = None
        b = None
        for digit in A:
            if res[digit-1] != 0:
                a = digit
            else:
                res[digit-1] = A[digit]
        for i in range(len(res)):
            if res[i] == 0:
                b = i+1
        return a, b


            
