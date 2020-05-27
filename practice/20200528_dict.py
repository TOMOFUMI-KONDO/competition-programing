# import sys

# def isHigh(str, compare):
#   if len(str) <= len(compare):
#     for i in range(len(str)):
#       if str[i] > compare[i]:
#         return True
#       elif str[i] < compare[i]:
#         return False
#     return False
#   else:
#     for i in range(len(compare)):
#       if str[i] > compare[i]:
#         return True
#       elif str[i] < compare[i]:
#         return False
#     return True

# def isLow(str, compare):
#   if len(str) <= len(compare):
#     for i in range(len(str)):
#       if str[i] < compare[i]:
#         return True
#       elif str[i] > compare[i]:
#         return False
#     return True
#   else:
#     for i in range(len(compare)):
#       if str[i] < compare[i]:
#         return True
#       elif str[i] > compare[i]:
#         return False
#     return False

# def main():
#     dictionary = []
#     n = int(input())
#     for _ in range(n):
#         order, str = input().split()

#         if order == 'insert':
#             len_dic = len(dictionary)
#             if len_dic > 1:
#                 L = 0
#                 R = len(dictionary) - 1
#                 M = (R + 1) // 2
#                 while M >= L:
#                     is_high = isHigh(str, dictionary[M-1])
#                     is_low = isLow(str, dictionary[M])
#                     if is_high and is_low:
#                         dictionary.insert(M, str)
#                         break
#                     elif is_high and not is_low:
#                         L = M
#                         if L == len(dictionary) - 1:
#                             dictionary.append(str)
#                             break
#                     elif not is_high and is_low:
#                         R = M - 1
#                         if R == 0:
#                             dictionary.insert(0, str)
#                             break
#                     else:
#                         print('予期せぬエラー')
#                         sys.exit(1)
#                     M = (L + R + 1) // 2
#             elif len_dic == 1:
#                 if isHigh(str, dictionary[0]):
#                     dictionary.append(str)
#                 else:
#                     dictionary.insert(0, str)
#             elif len_dic == 0:
#                 dictionary.append(str)
#             else:
#                 print('予期せぬエラー')
#                 sys.exit(1)

#         elif order == 'find':
#             len_dic = len(dictionary)
#             if len_dic > 1:
#                 L = 0
#                 R = len(dictionary) - 1
#                 M = (R + 1) // 2
#                 while M >= L:
#                     # print(L,R,M)
#                     if dictionary[M] == str:
#                         print('yes')
#                         break
#                     is_high = isHigh(str, dictionary[M])
#                     if is_high:
#                         L = M + 1
#                         if L > R:
#                             print('no')
#                             break
#                     else:
#                         R = M - 1
#                         if R < L:
#                             print('no')
#                             break
#                     M = (L + R + 1) // 2
#             elif len_dic == 1:
#                 if dictionary[0] == str:
#                     print('yes')
#                 else:
#                     print('no')
#             elif len_dic == 0:
#                 print('no')
#             else:
#                 print('予期せぬエラー')
#                 sys.exit(1)
#         else:
#             print('入力に誤りがあります。')
#             sys.exit(1)

# if __name__ == '__main__':
#     main()

# ↑自分で書いたやつ（TLEになった）
# ↓例解（こんな短くて済む）

SIZE = 13
POW = [1] * SIZE
for i in range(1, SIZE):
    POW[i] = POW[i-1] * 4
index = {'A': 1, 'G': 2, 'C': 3, 'T': 4}
DICT = [False]*POW[12] # 4^12個の要素

def getNum(s):
    global POW, index
    n = -1
    for i in range(len(s)):
        n += index[s[i]]*POW[i]

    return n

def main():
    global DICT
    n = int(input())

    for _ in range(n):
        c, s = input().split()

        if c == 'insert':
            DICT[getNum(s)] = True
        else:
            if DICT[getNum(s)]:
                print('yes')
            else:
                print('no')

if __name__ == '__main__':
    main()