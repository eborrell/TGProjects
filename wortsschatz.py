# -*- encoding: utf-8 -*-

import random as rnd

l = []
aux = ["art", "n", "t"]
f = open('NOUNS.rtf', 'r', encoding='utf-8')
text = f.read().split('\n')
c = 0
for line in text:
    aux = line.split('|')
    if len(aux)==3:
        l.append([aux[0], aux[1], aux[2]])
        c += 1

for i in range(0,10):
    p = rnd.randrange(0, c-1)
    t = l[p][2]
    a, n = input("\n" + l[p][2] + "\n").split(' ')
    if (a != l[p][0] or n != l[p][1]):
        print("Nein!" + l[p][0] + " " + l[p][1])

f.close()
