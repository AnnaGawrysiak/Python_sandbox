def simplify_string(word):
    output = []
    counter = 1
    output.append(word[0])

    for i in range(1, len(word)):
        if word[i] == word[i-1] and counter <= 1:
            counter = counter +1
            output.append(counter)
        elif word[i] == word[i-1] and counter > 1:
            counter = counter + 1
            output[-1] = counter
        else:
            counter = 1
            output.append(word[i])

    listToStr = ''.join([str(elem) for elem in output])

    return listToStr

text1 = "abcacc"
text2 = "xyz"
text3 = "mm"
text4 = "aabaaabbbb"

print(simplify_string(text1))
print(simplify_string(text2))
print(simplify_string(text3))
print(simplify_string(text4))

def expand_string(word):

    output = ""

    for i in range(len(word)):

         if word[i].isnumeric():
             output = output + word[i-1]*(int(word[i])-1)
         else:
             output = output + word[i]

    return output

word1 = simplify_string(text1)
word2 = simplify_string(text2)
word3= simplify_string(text3)
word4 = simplify_string(text4)

print(expand_string(word1))
print(expand_string(word2))
print(expand_string(word3))
print(expand_string(word4))


