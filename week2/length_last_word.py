class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        A = A.strip()
        last_word_count = 0
        for char in A:
            if char == ' ':
                last_word_count = 0
            else:
                last_word_count += 1
        return last_word_count
