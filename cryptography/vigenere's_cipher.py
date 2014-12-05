mylist = [ [0]*26 for i in range(26)]
for i in range(26):
  for j in range(26):
    n=i+97+j
    if(n>122):
      l=n-122
      l=l+96
      mylist[i][j]=chr(l)
    else:
      mylist[i][j]=chr(n)



key = raw_input('Enter the key string for the encryption: ')
mydata = raw_input('Enter the string to be encrypted : ')

if(len(key)<len(mydata)):
    n=len(mydata)-len(key)
    for i in range(n):
        if(i>len(key)):
            i=i-len(key)
            key=key+key[i-1]
        else:
            key=key+key[i]
       
cipher_text = ''

for i in range(len(mydata)):
    n=ord(key[i])-97
    m=ord(mydata[i])-97
    cipher_text=cipher_text+mylist[n][m]

print 'The encrypted code is :'
print cipher_text
