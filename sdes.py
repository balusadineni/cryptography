#Implementation of S_Des in python

def keygen():
    k=raw_input("Enter the key of 10 bits for encryption :")
    key1,key2=p10(k)
    return key1,key2

def p10(k):
    p10=[3,5,2,7,4,10,1,9,8,6]
    p10key=''
    for i in p10:
        p10key+=k[i-1]
    left,right=p10key[:len(k)/2],p10key[len(k)/2:]
    key1= lshift(left,right,1)
    key2= lshift(left,right,3)
    return key1,key2

def lshift(left,right,n):
    left=left[n:]+left[:n]
    right=right[n:]+right[:n]
    key=left+right
    k= p8(key)
    return k

def p8(k):
    p8=[6,3,7,4,8,5,10,9]
    p8key=''
    for i in p8:
        p8key+=k[i-1]
    k=p8key
    return k

def main():

    key1,key2=keygen()
    print key1
    print key2
    plain(key1,key2)

def plain(key1,key2):
    plaintext=raw_input("Enter the plain string of 8 bits for encryption :")
    k1=key1
    k2=key2
    ip(plaintext,k1,k2)

def ip(plaintext,key1,key2):
    ip=[2,6,3,1,4,8,5,7]
    ipkey=''
    for i in ip:
        ipkey+=plaintext[i-1]
    left,right=ipkey[:len(ipkey)/2],ipkey[len(ipkey)/2:]
    ebypkey=ebyp(right)
    left1,right1=xor(key1,ebypkey)
    p4key=sbox(left1,right1)
    xor1=xor4(p4key,left)
    x=right+xor1
    left2,right2=x[:len(x)/2],x[len(x)/2:]
    ebypkey2=ebyp(right2)
    left3,right3=xor(key2,ebypkey2)
    p42key=sbox(left3,right3)
    xor2=xor4(p42key,left2)
    y=xor2+right2
    ip_inv=ip_inverse(y)
    print "The encrypted bit string :",ip_inv

def ip_inverse(y):
    ipin=[4,1,3,5,7,2,8,6]
    ipinkey=''
    for i in ipin:
        ipinkey+=y[i-1]
    return ipinkey



def ebyp(r):
    ebyp=[4,1,2,3,2,3,4,1]
    ebypkey=''
    for i in ebyp:
        ebypkey+=r[i-1]
    return ebypkey

def xor4(a,b):
    xor4key=''
    for i in range(len(a)):
        xor4key+=str(int(a[i])^int(b[i]))
    return xor4key


def xor(k,e):
    xorkey=''
    for i in range(len(k)):
xorkey+=str(int(k[i])^int(e[i]))
    left,right=xorkey[:len(k)/2],xorkey[len(k)/2:]
    return left,right

def sbox(l,r):
    s0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    s1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
    row0,col0 = int((l[0]+l[3]),2),int((l[1]+l[2]),2)
    s0key="{0:b}".format(s0[row0][col0])
    if len(s0key) == 1:
        s0key='0'+s0key
    row1,col1=int((r[0]+r[3]),2),int((r[1]+r[2]),2)
    s1key="{0:b}".format(s1[row1][col1])
    if len(s1key) == 1:
       s1key='0'+s1key
    skey=s0key+s1key
    p4=[2,4,3,1]
    p4key=''
    for i in p4:
        p4key+=skey[i-1]
    return p4key



main()
