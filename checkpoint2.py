class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        res = [[1]]
        if A == 1:
            return res
            
        for i in range(2, A+1):
            size = (2 * i) - 1
            self.build_layer(res, i, size)
        return res
    
    def build_layer(self, data, i, n):
        for row in data:
            row.insert(0, i)
            row.append(i)
        #add_top:
        data.insert(0, [i]*n)
        #add_bottom
        data.append([i]*n)
