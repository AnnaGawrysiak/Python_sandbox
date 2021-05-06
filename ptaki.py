import ast

text = ""

with open("jakis_akapit.txt", mode='r', encoding='utf-8') as file1:
    for line in file1:
        text += line

file2 = open("nazwy.txt", mode= "r")

contents = file2.read()
dictionary = ast.literal_eval(contents)

file2.close()

li = list(text.split(" "))

punctuation = ""

for index, item in enumerate(li):
    if item[-1] == "." or item[-1] == ',':
        punctuation = item[-1]
        item = item[0: (len(item)-1)]
    if item in dictionary:
        bird = item + " (" + dictionary[item] + ")" + punctuation
        li[index] = bird
    punctuation = ''

mystring = ' '.join(li)

print(mystring)

birds = open("Output.txt", mode="w")
birds.write(mystring)
birds.close()