# def jest_palindromem(text):
#
#     ostatni = len(text)-1
#
#     for i in range(len(text)//2):
#         if text[i] != text[ostatni-i]:
#             return False
#
#     return True
#
# zmienna = "anna"
#
# if jest_palindromem(zmienna):
#     print(zmienna, " jest palindromem")
# else:
#     print(zmienna, "nie jest palindromem")

# wszystkie liczby 4-cyfrowe, max 10 iteracji

# for i in range(1, 10):
#     tysiace = i
#     for j in range(0, 10): # range jest asymetryczna
#         setki = j
#         for k in range(0, 10):
#             dziesiatki = k
#             for l in range(0, 10):
#                 jednosci = l
#                 liczba = 1000 * tysiace + 100 * setki + 10 * dziesiatki + jednosci
#                 print(liczba)
#
#plik = open("plik_binarny.bin", "rb")
#plik = open("plik_binarny.bin", "wb")
# liczby = [1,2,3,5]
# bin_liczby = bytearray(liczby)
# line = plik.readline()
# for line in plik.readlines():
# #     print(line)
# #print(plik.read(3))
#
# file = open("plik_zwykly.txt", "r")
#
# # liczby = [1, 2, 3, 4, 5]
# # file.write(str(liczby))
# for line in file.readlines():
#     print(line)
#
# file.close()

with open("plik_zwykly.txt", "a") as file:
    file.write("kolejna")



