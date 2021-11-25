# this program shows each of integer subsets in given list of integer numbers
class Program:
    def __init__(self, nums):
        self.nums = nums
    def sub(self):
        list1 = self.nums.split()
        list2 = list(list1)
        list3 = []
        list4 = []
        list4.append(list2)
        m = 1
        while(True):
            for i in range(0, len(list1)):
                list1.remove(list1[i])
                list3 = list(list1)
                if list4.count(list3) == 0:
                    list4.append(list3)
                list1 = list(list2)
            list1 = list(list4[m])
            list2 = list(list4[m])
            if len(list1) == 1:
                break
            m += 1
        print(list4)
nums = Program(input())
nums.sub()

