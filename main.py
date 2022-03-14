import pandas as  pd
import numpy as np



googleSheetId = "1pEroBjP1UZMCNBu0Gju0WBH_zUiQDC_IjZMOu72CbR0"
worksheetName = "OG"
URL = "type google sheet url with output as csv ".format(
	googleSheetId,
	worksheetName
)

df = pd.read_csv(URL)


#or just import and use df = pd.read_csv("data.csv")


x1 = df.coloumn1.to_list()
x2 = df.coloumn2.to_list()
x3 = df.coloumn3.to_list()
x4 = df.coloumn4.to_list()
x5 = df.coloumn5.to_list()
x6 = df.coloumn6.to_list()
x7 = df.coloumn7.to_list()

code = ["j","p","o","v","i","t","a"]
load = [x1,x2,x3,x4,x5,x6,x7]



c = input("find code: ")
b = str(input("for code : "))
a = str(input("data to search : "))


# I named the following code as Paul's sky sequence1

i = [x for x in range(0,len(xn))]
i2 = [x for x in range(0,len(load))]

for new in i2:
    if c in code[new]:
        first = load[new]
    elif c in code[new]:
        second = load[new]

for n in i2:
    if c in str(code[n]):
        first = load[n]
    elif b in str(code[n]):
        p = coloumn[n]


for q in i:
    if a in str(first[q]):
        print (df.to_numpy()[q][p])