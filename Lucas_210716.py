print("question 2")
Bpython={"string":"friend",
         "number":1475,
         "list":["bread","chesse"],
         1:{"food":"yakioba","dog":"Cacau"},
         2:2==2,
         3:(2,4,1)}
print("question 3")
print(Bpython)
print("question 4")
s=""
for dp in Bpython.keys():
    s=s.lstrip()+" "+str(dp)
print(s)
print("question 5")
print(Bpython["string"])
print("question 6")
for suf, fsu in Bpython.items():
    print(suf)
    print(fsu)
print("question 7")
A=[]
for lo in Bpython.keys():
    A.append(str(lo))
A.sort()
A.reverse()
print(A)
print("question 8")
bd={}
for lists in range(10):
    nol="L"+str(lists)
    lh=list(range(lists+1))
    bd[nol]=lh
print("question 9")
for lp in bd.values():
    print(lp)