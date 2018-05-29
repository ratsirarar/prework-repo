class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        return self.is_colorful(str(A))
    
    def mult(self, num):
        num = int(num)
        if num == 0:
            return 0
        res = 1
        while num // 10 or num % 10:
            res *= num % 10
            num = num // 10
        return str(res)
    
    def is_colorful(self, A):
        colorful = {}
        for i in range(len(A)):
            j = 0
            end = j + i + 1
            while end <= len(A):
                res = self.mult(A[j: end])
                if colorful.get(res):
                    return 0
                else:
                    colorful[res] = 1
                end += 1
        return 1
