mydict = {'Aftermath': 'The Rolling Stones', 'Achtung Baby': 'U2', 'The Sensual World': 'Kate Bush', 'Invisible Touch': 'Genesis'}

#wyswietlanie wszystkich kluczy
def print_keys(mydict):
    for key in mydict:
        print( key)

print_keys(mydict)
#pobiera od użytkownika listę i sprawdza czy odpowiada on kluczowi (właściwie liście kluczy) ze słownika.
# hint: coś z sortowaniem

def is_match(mydict, another_dictionary):
    list_of_keys1 = sorted(mydict.keys())
    list_of_keys2 = sorted(another_dictionary.keys())

    for a, b in zip(list_of_keys1, list_of_keys2):
        if(a != b):
            return False
    return True

another_dictionary1 = { }
another_dictionary1.update({"The Dark Side of The Moon": "Pink Floyd", "Out of myself": "Riverside"})
another_dictionary1["Wishmaster"] = "Nightwish"

another_dictionary2 = {'Aftermath': 'The Rolling Stones', 'Achtung Baby': 'U2', 'The Sensual World': 'Kate Bush', 'Invisible Touch': 'Genesis'}

if is_match(mydict, another_dictionary1):
    print( "Dictionaries contain the same keys. ")
else:
    print("Keys are different. ")

if is_match(mydict, another_dictionary2):
    print( "Dictionaries contain the same keys. ")
else:
    print("Keys are different. ")

# Dodatkowo chcemy, aby nam odpowiedział kto jest wykonawcą w przypadku gdy już podaliśmy go wcześniej.
# Jeśli tak, to drukujemy odpowiedni komunikat, np.: "Wykonawcą albumu "Achtung baby" jest U2".
# W przeciwnym razie wyświetlany jest komunikat: "Brak danych".

artist = input("Type in name of the album. ")
try:
    print(" Wykonawca albumu ", mydict[artist], "jest", artist)
except:
    print("Brak danych. ")

# Zmodyfikuj kod powyżej dodatkowo tak, aby możliwe było dodawanie i usuwanie przez użytkownika informacji o nowych albumach do słownika.
# (np poprzez jakieś składnie w stylu "usun Invisible Touch" lub "dodaj Abbey Road by The Beatles")
def usun(mydict, album):
    del(mydict[album])
def dodaj(mydict, album, artysta):
    mydict[album] = artysta

dodaj(mydict, "Lateralus", "Tool")
# choice = print ("Nacisnij 1, jesli chcesz dodac album. Nacisnij 2, jesli zamierzasz go usunac. Nacisnij 3, jesli chcesz wyjsc z programu.")
#     case '1':
#         title = input("Wpisz album, ktory chcesz dodac: ")
#         artist = input("Wskaz wykonawce: ")
#         dodaj(mydict, title, artist)
#     case '2':
#         title = input("Wpisz album, ktory chcesz usunac: ")
#         usun(mydict, title)
#     case '3':
#         break

print_keys(mydict)