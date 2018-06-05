class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        # we want to find a divider in A and B such that
        # m <= n this is so that j is always positive
        # i + j = m - i + n - j + 1
        # A[i-1] <= B[j] and B[j-1] <= A[i]
        
        # find best i which will give us j = ((m + n + 1)/2) - i
        
        # if A[i - 1] > B[j] search left
        # if A[i] < B[j-1] search right
        
        
        median = 0
        
        if len(A) >  len(B):
            #insure that j is positive
            A, B = B, A
        
        m = len(A)
        n = len(B)
        
        if len(A) == 0:
            if n % 2 > 0: #odd
                return B[n/2]
            else: #even
                mid = n/2
                return (B[mid-1] + B[mid])/2.
        
        imin = 0 
        imax = m
        # print A, B
        while imin <= imax:
            i = (imin + imax) / 2
            j = ((m + n + 1) / 2 ) - i
            # print A[i], B[j]

            if i > 0 and A[i-1] > B[j]:
                imax = i - 1
            elif i < m and A[i] < B[j-1]:
                imin = i + 1 
            else: #A[i-1] <= B[j] and B[j-1] <= A[i]:
                break
                
        if (m+n) % 2 == 0:
            if i == m:
                median = B[j-1]
            elif j == n:
                median = A[i-1]
            print imin, imax, i, j#, max(A[i-1], B[j-1]), min(A[i], B[j])
            median = (max(A[i-1], B[j-1]) + min(A[i], B[j])) / 2.
        else:
            # print imin, imax, i, j#, max(A[i-1], B[j-1]), min(A[i], B[j])
            # print m == i
            if i == m:
                median = B[j]
            elif j == n:
                median = A[i]
            else:
                median = min(A[i], B[j])
            
        return median
                
                
                
                
                
            
