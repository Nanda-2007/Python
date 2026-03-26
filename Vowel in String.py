str=input()
c=True
for i in str:
    if i in 'aeiouAEIOU':
        c=False
        print('Vowel Found:',i)
        break
if c:
    print('Vowel Not Found!!')
