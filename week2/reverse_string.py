class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        res = []
        A = A.split("\s")
        A = [i.strip() for i in A if i]
        
        for i in range(len(A)):
            res.append(A[len(A)-1-i])
        return " ".join(res)
        
