import re

text = ' '

t = open('Dictionary.txt', 'r')
m = open('a_index', 'r')
n = open('word.txt', 'r');
p = open('a_data','r');

for line in t:                  
    text += ' ' + line              ##read entire dictionary in one line 'text'

for line in m:
    text += ' ' + line

for line in n:
    text += ' ' + line

for line in p:
    text += ' ' + line
    
k = open('notpresent.txt', 'r')
h = open('hihi.txt','w')
f = open('not_present.txt','w')

sep = r'(-|/|,)'
for line in k:
    if "-" in line:
        words = line.split("-")
        for word in words:
            if word in text:
                f.write(word)
                break
    elif "," in line:
        words = line.split(",")
        for word in words:
            if word in text:
                f.write(word)
                break
    elif "/" in line:
        words = line.split("/")
        for word in words:
            if word in text:
                f.write(word)
                break
    else:
        h.write(line)

k.close()
h.close()
f.close()

d =  open('Finally_found.txt', 'w')
t =  open('Kachra.txt', 'w')
p = open('hihi.txt','r')
for line in p:
    flag = 1
    for i in range(9, len(line),3):
        k = line[0:i]
        if k in text:
            t.write(k+'\n')
            flag = 0
            break
    if flag == 1:
        d.write(line)
d.close()
t.close()
