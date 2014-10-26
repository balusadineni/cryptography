ilename = argv
#it needs some file name
#charecter analysis of frequency
from  sys import argv

script, f
txt = open(filename)

print "Here's your file %r:" % filename
string=  txt.read()
string = string.replace(" ", "")
print string
my_list = [[0]*2 for i in range(26)]
my_list = [[0]*2 for i in range(26)]
for i in range(26):
    for j in range(2):
        my_list[i][0]=chr(97+i)

for j in range(len(string)-1):
    n =  ord(string[j])
    l=n-97
    my_list[l][1] = my_list[l][1]+1

print my_list



