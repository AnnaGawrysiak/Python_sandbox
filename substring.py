def issubstring(text, pattern):

    pattern_index = 0
    position_in_text = 0

    while(pattern_index < len(pattern) and position_in_text < len(text)):
        if(text[position_in_text] != pattern[pattern_index]):
            pattern_index = -1
            position_in_text = position_in_text - pattern_index -1

        pattern_index += 1
        position_in_text += 1

    if(pattern_index == len(pattern)):
        return True
    else:
        return False

# text1 = 'salamandra'
# text2 = 'la'
text1 = 'lalo'
text2 = 'lala'

if(issubstring(text1, text2)):
    print(text2, ' is a part of ', text1)
else:
    print(text2, ' is not a part of ', text1)