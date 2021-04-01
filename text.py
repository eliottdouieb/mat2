def revword(word):
    result=" "
    count_pos_letter=len(word)
    while count_pos_letter >0:
        result=result+word[count_pos_letter-1]
        count_pos_letter=count_pos_letter-1
    return result.strip().lower()

##def countword():
fm=open('C:/Users/eliot/Desktop/mat2/text.txt')
word=""
for row in fm:
    word=row.strip()
    break
count=0
for row in fm :
    words=row.split()
    for i in range(len(words)):
        words[i]=revword(words[i])
        if words[i]==word:
            count=count+1
print(count+1)









