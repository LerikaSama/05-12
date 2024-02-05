#class Fib:
#    def __init__(self, nn):
#       print("__init__")
#       self.__n == nn
#        self.__i = 0
#        self.__p1 = self.__p2 = 1
#
#     def __iter__(self):
#         print("__iter__")
#         return self
#
#     def __next__(self):
#         print("__next__")
#         self.__i +=1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret
#
# for i in Fib(10):
#     print(i)

#########################################################

# class Fib:
#     def __init__(self, nn):
#         self.__n == nn
#         self.__i = 0
#         self.__p1 = self.__p2 == 1
#
#     def __iter__(self):
#         print("Fib iter")
#         return self
#
#     def __next__(self):
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2. ret
#         return ret
#
# class Class:
#     def __init__(self, n):
#         print("Class iter")
#         return self.__iter;
#
# object = Class(8)
#
# for i in object:
#     print(i)


###################################

# def fun(n):
#     for i in range(n):
#         yield i
#
# print(fun(5))

##################################


#####################################
# def powersOf2(n):
#     pow = 1
#     for i in range(n):
#         yield pow
#         pow *= 2
# for v in powersOf2(8):
#     print(v)

##########################################
# def powersOf2(n):
#     pow = 1
#     for i in range(n):
#         yield pow
#         pow *= 2
#
# t = [x for x in powersOf2(5)]
#
# print(t)

##################################
#
# def powersOf2(n):
#     pow = 1
#     for i in range(n):
#         yield pow
#         pow *= 2
#
# t = list(powersOf2(3))
#
# print(t)
# #
#
# #################################
#
# def powersOf2(n):
#     pow = 1
#     for i in range(n):
#         yield pow
#         pow *= 2
# for i in range(20):
#     if i in powersOf2(4):
#         print(i)
#
# ###########################
#
# def Fib(n):
#     p = pp = 1
#     for i in range(n):
#         if i in [0, 1]:
#              yield 1
#         else:
#             n = p + pp
#             pp, p = p, n
#             yield n
#
# fibs = list(Fib(10))
#
# print(fibs)
# #
# ###########################

# lst = [1 if x % 2 == 0 else 0 for x in range(10)]
# genr = (1 if x % 2 == 0 else 0 for x in range(10))
# for v in lst:
#     print(v, end=" ")
# print()
#
# for v in genr:
#     print(v, end=" ")
# print()

##################################
# two = lambda : 2
# sqr = lambda x : x * x
# pwr = lambda x, y : x ** y
#
# for a in range(-2, 3):
#     print(sqr(a), end=" ")
#     print(pwr(a, two()))

#################################

# divide_to_two = lambda x: x / 2
#      #одно и тоже
# def divide_to_two(x):
#     return x / 2

#######################


# list1 = [x for x in range(5)] # диапозон
# list2 = list(map(lambda x: 2 ** x, list1)) #мап позволяет прописать
# print(list2)
# for x in map(lambda x: x * x, list2):
#     print(x, end=' ')
# print()

####################

# list_num = [1, 2, 3, 4, 5]
# my_list = list(map(lambda x: x * 2, list_num))
# #lambda заменяет for, list позволяет записать все в вписок
#
# print(list_num)
# print(my_list)

############################################
list_num = [1, 2, 3, 4, 5]

my_list = list(filter(lambda x: x % 2 == 0, list_num))
#фильтр работает как мап, только с условием, если правдиво запишет. если нет то нет

print(list_num)
print(my_list)