#cipher encryption pyhton
flag=''
a=raw_input("enter 1 for encryption or enter 2 for decryption : ")
if(a==1):
    encstr=raw_input("enter the key to be encrypted :: ")
    for j in range(1,26):
        for i in range(len(encstr)):
            num=ord(encstr[i])
            num=num+j
            if(num>122):
                x=num-122
                num=x+96
                flag=flag+chr(num)
            else:
                flag=flag+chr(num)
        print flag
        flag=''
else:
    decstr=raw_input("enter the encrypted string to be decrypted ::")
    for k in range(1,26):
        for l in range(len(decstr)):
            nu=ord(decstr[l])
            nu=nu-k
            if(nu<97):
                y=97-nu
                nu=123-y
                flag=flag+chr(nu)
            else:             
                flag=flag+chr(nu)
        print flag
        flag=''

            
    
