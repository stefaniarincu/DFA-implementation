def acceptare(DFA, s, final, nod_act, tr):
    tr.append(nod_act)
    for j in range(len(s)):
        if s[j] not in DFA[nod_act]:
            return 'NU'
        nod_act = DFA[nod_act][s[j]]
        tr.append(nod_act)
    if nod_act in final:
        return 'DA', tr
    else:
        return 'NU'

n, m = input().split()
n = int(n)
m = int(m)
DFA = {}
for i in range(0, m, 1):
    x, y, val = input().split()
    if int(x) not in DFA:
        DFA[int(x)] = {}
    DFA[int(x)][val] = int(y)
nod_inc = int(input())
final = [int(x) for x in input().split()]
k = int(input())
list = []
for i in range(0, k):
    s = input()
    list.append(s)

for s in list:
    tr = []
    acc, tras = acceptare(DFA, s, final, nod_inc, tr)
    if acc == 'N':
        print("NU")
    else:
        print(acc)
        print("Traseu:", end = " ")
        for i in tras:
            print(i, end = " ")
        print()