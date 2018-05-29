class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        root = A
        part_1, mid, part_2 = self.find_middle(A)
        if not part_2:
            #Only one element
            return 1
        # self.printMe(part_1)
        # self.printMe(mid)
        # self.printMe(part_2)
        part_2 = self.reverse(part_2)
        # self.printMe(part_2)
        return self.is_identical(part_1, part_2)

    def is_identical(self, part_1, part_2):
        while part_1 and part_2:
            if part_1.val != part_2.val:
                return 0
            part_1 = part_1.next
            part_2 = part_2.next

        if part_1 or part_2:
            return 0
        return 1

    def reverse(self, A):
        curr = A
        prev = None #This will be the root node

        while curr:
            tmp_next_node = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next_node

        return prev

    def find_middle(self, A):
        part_1 = A
        part_2 = None

        step1 = part_1
        step2 = self._2_steps(part_1)

        mid = None
        prev_step1 = step1
        

        while type(step2) != int:
            prev_step1 = step1
            step1 = step1.next
            step2 = self._2_steps(step2)

        #Split List
        if step2 == -1:
            #ODD
            mid = step1
            prev_step1.next = None
            part_2 = mid.next
            mid.next = None
        else:
            #EVEN
            part_2 = step1.next
            step1.next = None

        return part_1, mid, part_2

    def _2_steps(self, A):
        curr = A.next
        if curr == None:
            #This is Odd because the 1st step is Null
            return -1
        curr = curr.next
        if curr == None:
            #this is Even because the second step is null
            return 0
        return curr

    def get_list_from_arr(self, A):
        root = Node(A[0])
        prev = root
        for i in range(1, len(A)):
            curr = Node(A[i])
            prev.next = curr
            prev = curr
        return root

    def get_arr_from_list(self, A):
        curr = A
        while curr is not None:
            print(curr.val)
            curr = curr.next

    def printMe(self, A):
        print(self.get_arr_from_list(A))
