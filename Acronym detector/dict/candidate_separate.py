import re
count = 0
text = ' '
f= open('India.txt', 'r')
g = open('present.txt', 'w')
k = open('notpresent.txt', 'w')
t = open('Dictionary.txt', 'r')
m = open('a_index', 'r')
n = open('word.txt', 'r');
p = open('a_data','r');

lett = r'(०|१|२|३|४|५|६|७|८|९|1|2|3|4|5|6|7|8|9|0)'
for line in t:                  
    text += ' ' + line              ##read entire dictionary in one line 'text'

for line in m:
    text += ' ' + line

for line in n:
    text += ' ' + line

for line in p:
    text += ' ' + line
    
for line in f:
    words = line.split()
    for word in words:
        word = word.strip(",[]()|'\"\.");
        if (word in text) or re.search(lett, word):           ##check for dictionary words
            g.write(word+'\n')
        else:
            k.write(word+'\n')
        

g.close()
k.close()
t.close()
f.close()
m.close()
n.close()
p.close()
print 'finished'
