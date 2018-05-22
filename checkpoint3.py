class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        C = [a for a in A]
        return self.quick_select(C, 0, len(C)-1, B-1) 
    
    def quick_select(self, A, s, e, k):
        if s > e:
            return -1
        index = self.partition(A, s, e)
        if k == index:
            return A[index]
        elif k < index:
            return self.quick_select(A, s, index-1, k)
        else:
            return self.quick_select(A, index+1, e, k)
    
    def partition(self, A, s, e):
        key = A[s]
        i, j = s+1, e
        
        while i < j:
            while i <= e) and A[i] <= key:
                i += 1
            while j > s and A[j] >= key:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
                
        index = j
        
        if key > A[j]:
            A[s], A[j] = A[j], A[s]
        else:
            index = s
        return index
                
    
    
    
