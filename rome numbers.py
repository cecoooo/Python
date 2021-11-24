class Numbers:
    def __init__(self, num):
        self.num = num
    def roman_nums(self):
        num = self.num
        str = ''
        while(True):
            if num >= 4000:
                print('number too large')
                break
            elif num >= 1000:
                str += 'M'
                num -= 1000
            elif num >= 900 and num < 1000:
                str += 'CM'
                num -= 900
            elif num >= 500 and num < 900:
                str+='D'
                num -= 500
            elif num >= 400 and num < 500:
                str += 'CD'
                num -= 400
            elif num >= 100 and num < 400:
                str += 'C'
                num -= 100
            elif num >= 90 and num < 100:
                str += 'XC'
                num -= 90
            elif num >= 50 and num < 90:
                str += 'L'
                num -= 50
            elif num >= 40 and num < 50:
                str += 'XL'
                num -= 40
            elif num >= 10 and num < 40:
                str += 'X'
                num -= 10
            elif num == 9:
                str += 'IX'
                num -= 9
            elif num >= 5 and num < 9:
                str += 'V'
                num -= 5
            elif num == 4:
                str += 'IV'
                num -= 4
            elif num > 0:
                str += 'I'
                num -= 1
            else:
                break
        print(str)
    def nums(self):
        str = self.num
        num = 0
        for i in range(0, len(str)):
            if str[i] == 'M':
                num += 1000
            elif str[i] == 'D':
                num += 500
            elif str[i] == 'C':
                if i != len(str) - 1:
                    if str[i+1] == 'M':
                        num += 900
                        continue
                    elif str[i+1] == 'D':
                        num += 400
                        continue
                num += 100
            elif str[i] == 'L':
                num += 50
            elif str[i] == 'X':
                if i != len(str) -1:
                    if str[i+1] == 'C':
                        num += 90
                        continue
                    elif str[i+1] == 'L':
                        num += 40
                        continue 
                num += 10
            elif str[i] == 'V':
                num += 5
            elif str[i] == 'I':
                if i != len(str) - 1:
                    if str[i+1] == 'X':
                        num += 9
                        continue
                    elif str[i+1] == 'V':
                        num += 4
                        continue
                num += 1
        print(num)

text = input('Enter what kind of number you need: ')
if text == 'roman':
    num = Numbers(int(input('Enter number: ')))
    num.roman_nums()
else:
    num = Numbers(input('Enter roman number: '))
    num.nums()

# class py_solution:
#     def int_to_Roman(self, num):
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#             ]
#         syb = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#             ]
#         roman_num = ''
#         i = 0
#         while  num > 0:
#             for _ in range(num // val[i]):
#                 roman_num += syb[i]
#                 num -= val[i]
#             i += 1
#         return roman_num


# print(py_solution().int_to_Roman(1))
# print(py_solution().int_to_Roman(4000))