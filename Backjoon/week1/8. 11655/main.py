word = input()

encode = ''

for i in range(len(word)):
    if word[i].isalpha():
        if (ord(word[i])>64 and ord(word[i])<78) or (ord(word[i])>96 and ord(word[i])<110):
            encode += chr(ord(word[i]) + 13)
        else:
            encode += chr(ord(word[i]) - 13)
    else:
        encode += word[i]

print(encode)