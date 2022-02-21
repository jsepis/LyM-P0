import re

linea="(move-dir n D)"
lineaList=re.split(r'[ ()]',linea)
for i in lineaList:
    if i=='':
        lineaList.remove(i)

try:
    lineaList[2]
    b=True
except IndexError:
    b =False
n="3"

if n =="1" or n=="2":
    print("yes")
else: print("no")

