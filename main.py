# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
#
# Examples
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
# Notes
# The number can be negative already, in which case no change is required.
# Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
# def make_negative( number ):
#     return number - (number*2) if number > 0 else number
# print(make_negative(5))


# def rps(p1, p2):
#     if p1 == 'scissors' and p2 == 'paper':
#         return "Player 1 won!"
#     elif p1 == 'scissors' and p2 == 'rock':
#         return "Player 2 won!"
#
#
#     elif p1 == 'paper' and p2 == 'scissors':
#         return "Player 2 won!"
#     elif p1 == 'paper' and p2 == 'rock':
#         return "Player 1 won!"
#
#     elif p1 == 'rock' and p2 == 'scissors':
#         return "Player 1 won!"
#     elif p1 == 'rock' and p2 == 'paper':
#         return "Player 2 won!"
#
#     elif p1 == p2 or p2 == p1:
#         return "Draw!"
#     else:
#         return "Error"
# rps('paper', 'paper')




# def count_sheeps(arrayOfSheeps):
#     return arrayOfSheeps.count(True)
#
# print(count_sheeps([True,  True,  True]))

# def count_sheeps(array_of_sheep):
# # TODO May the force be with you
#   count = 0
#   for sheep in array_of_sheep:
#       if sheep:
#           count += 1
#   return count
# print(count_sheeps([True, False, True]))


# def basic_op(operator, value1, value2):
#     if operator == '/':
#         return value1 / value2
#     elif operator == '*':
#         return value1 * value2
#     elif operator == '+':
#         return value1 + value2
#     elif operator == '-':
#         return value1 - value2
#     else:
#         return 'Error'
# def basic_op(operator, value1, value2):
#     return eval(f'{value1}{operator}{value2}')
# print(basic_op('-', 12, 5))


# def abbrev_name(name):
#     return (name[0]).capitalize() + '.' + (name[name.find(' ') + 1]).capitalize()
#
#
#
# print(abbrev_name('Sam Harris'))
#
# def abbrevName(name):
#     first, last = name.upper().split(' ')
#     return first[0] + '.' + last[0]



# def to_jaden_case(string):
#     return ' '.join(word.capitalize() for word in string.split())
#
#
#
#
# print(to_jaden_case('How can mirrors be real if our eyes arent real'))


# def is_square(n):
#     if n >= 0:
#         return True if (n ** 0.5).is_integer() else False
#     else:
#         return False
#
# print(is_square(-1))


# import math
# def nb_year(p0, percent, aug, p):
#     i = 0
#     while p0 < p:
#         p0 = p0 + math.floor(p0 * (percent / 100)) + aug
#         i += 1
#     return i
#
#
#
# nb_year(1500000, 2.5, 10000, 2000000)



# def valid_braces(string):
#     result = list(string)
#     bracket_1 = result.count('(')
#     bracket_2 = result.count(')')
#     curly_1 = result.count('{')
#     curly_2 = result.count('}')
#     parentheses_1 = result.count('[')
#     parentheses_2 = result.count(']')
#     if bracket_1 == bracket_2 and curly_1 == curly_2 and parentheses_1 == parentheses_2:
#         if
#     else:
#         return False
#
#
#
#
# print(valid_braces('[(])'))





# def points(games):
#     count = 0
#     for score in games:
#         res = score.split(':')
#         print(res)
#         if res[0]>res[1]:
#             count += 3
#         elif res[0] == res[1]:
#             count += 1
#     return count
# print(points(['3:2', '5:8', '7:9', '3:2', '5:8', '7:9',  '3:2', '5:8', '7:9', '9:8']))



# def find_it(seq):
#     for i in seq:
#         if seq.count(i) % 2 != 0:
#             return i
#
#
# print(find_it([0,1,0,1,0]))


# def order(words):
#   return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
#
#
# print(order("is2 Thi1s T4est 3a"))
#
# def order(s):
#     z = []
#     for i in range(1,10):
#         for j in list(s.split()):
#             if str(i) in j:
#                z.append(j)
#     return " ".join(z)



# def solution(number):
#     result = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             result += i
#             print(result)
#     return result
#
#
# print(solution(200))


# def solution(roman):
#     for s in roman:
#         m = roman.count('M') * 1000
#         d = roman.count('D') * 500
#         c = roman.count('C') * 100
#         l = roman.count('L') * 50
#         x = roman.count('X') * 10
#         v = roman.count('V') * 5
#         i = roman.count('I') * 1
#         iv = roman.count('iv') * 4
#         result = i + v + x + l + c + d + m
#
#     return result
#
#
# print(solution('MXIV'))

# def spin_words(sentence):
#     sentence = sentence.split(' ')
#     result = ''
#     for sentence in sentence:
#         if len(sentence) < 5:
#             result += ''.join(sentence) + ' '
#         else:
#             result += ''.join(reversed(sentence)) + ' '
#     result = result[:-1]
#
#     return result
#
# print(spin_words('Hey fellow warriors'))

# Можно было решить так

# def spin_words(sentence):
#     return ' '.join(i[::-1] if len(i) > 4 else i for i in sentence.split(' '))
#
#
# print(spin_words('Hey fellow warriors'))


# def reverse_alternate(s):
#     s = s.split()
#     result = ''
#     q = 0
#     for s in s:
#         if q % 2 != 0:
#             result += ''. join(reversed(s)) + ' '
#         else:
#             result += ''.join(s) + ' '
#         q += 1
#     result = result[:-1]
#     return result

# print(reverse_alternate('This is sparta man'))


# Можно было решить так

# def reverse_alternate(s):
#   return ' '.join(w[::-1] if i % 2 else w for i, w in enumerate(s.split()))
#
# print(reverse_alternate('This is sparta man'))





# fasfafa

# def digital_root(n):
#     number = [int(i) for i in str(n)]
#     while sum(number) >= 10:
#         number = [int(i) for i in str(sum(number))]
#
#     return sum(number)
# print(digital_root(493193))

# Можно было так

# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))
#
#
# print(digital_root(132189))



# def likes(names):
#     if len(names) == 0:
#         return 'no one likes this'
#     elif len(names) == 1:
#         return f'{names[0]} likes this'
#     elif len(names) == 2:
#         return f'{names[0]} and {names[1]} like this'
#     elif len(names) == 3:
#         return f'{names[0]}, {names[1]} and {names[2]} like this'
#     else:
#         return f'{names[0]}, {names[1]} and {len(names) - 2} like this'
#
#
# likes(['Peter', 'ALex', 'Nikita', 'Michel'])





# def array_diff(a, b):
#     return[i for i in a if i not in b]
# print(array_diff([1,2,2,2,3],[2]))



# def find_missing_letter(chars):
#     x = 'a b c d e f g h i j k l m n o p q r s t u v w x w z'
#     x = x.split()
#     return [i for i in chars if i not in x]


    # # print(x)
    # # for chars in chars:
    # #     # print(x)
    # #     for x in x:
    # #             print(x, chars)
    # print(set(chars).symmetric_difference(x))

    # chars = ''.join(chars)
    # for char in chars:
    #
    #     for x in x:
    #         print(x, char)



# print(find_missing_letter(['a','b','c','d','f']))




# def divisors(n):
#     return len([str(i) for i in range(1, n + 1) if n % i == 0])
# print(divisors(15))



def possibilities(param):
    i = [0, 1]
    for i in param:
        if i == '?':
