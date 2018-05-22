class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        d = {i:0 for i in A}
        longest = 1
        for elm in A:
            tmp_longest = 1
            key = elm - 1
            if not d.get(key):
                while d.get(elm+1) != None:
                    tmp_longest += 1
                    elm += 1
            if longest < tmp_longest:
                longest = tmp_longest
        return longest
