word = input()
for i in range(len(word)//2+1):
    if word[i] == word[len(word)-i-1]:
        result = 1
    else:
        result = 0
        break
print(result)        
    