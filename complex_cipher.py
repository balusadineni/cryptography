flag = ''
op = raw_input("Enter the option 1 to encrypt and 2 to decrypt :")
if(op==1):
    enc_str = raw_input("Enter the string to be encrypted in ceaser cipher :")
    for n in range(1,26):
        for m in ragne(len(enc_str)):
            if(ord(enc_str[m])!=32):
                num=ord(encstr[m])
                if((num>=97) and (num<=122)):
                    num=num+n
                    if(num>122):
                        x=num-122
                        num=x+96
                        flag=flag+chr(num)
                    else:
                        flag=flag+chr(num)
                elif((num>=65) and (num<=90)):
                    num=num+n
                    if(num>90):
                        y=num-90
                        num=y+65
                        flag=flag+chr(num)
                    else:
                        flag=flag+chr(num)
                else:
                    flag=flag+enc_str[m]
            else:
                flag=flag+enc_str[m]
        print flag
        flag=''
else:
     dec_str = raw_input("Enter the Encrypted string to decrypt :")
     for n in range(1,26):
         for m in range(len(dec_str)):
             if(ord(dec_str[m])!=32):
                 num=ord(dec_str[m])
                 if((num>=97) and (num<=122)):
                     num=num-n
                     if(num<97):
                         y=97-num
                         num=123-y
                         flag=flag+chr(num)
                     else:
                         flag=flag+chr(num)
                 elif((num>=65) and (num<=90)):
                     num=num-n
                     if(num<65):
                         y=65-num
                         num=90-y
                         flag=flag+chr(num)
                     else:
                         flag=flag+chr(num)
                 else:
                     flag=flag+dec_str[m]
             else:
                 flag=flag+dec_str[m]
         print flag
         flag=''   
