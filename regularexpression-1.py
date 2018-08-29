#1
import re
a=('the text is uppal.tushar98@gmail.com test')
b=list(a.split(' '))
for i in b:
    match=re.finditer('^[\w]*(@)(gmail.com|yahoo.com)',i)
    for i in match:
        print(i.group())


#2
import re
a=('the text is +918894897895')
b=list(a.split(' '))

for i in b:
    match=re.finditer('^[+91][6-9][0-9]{11}',i)
    for i in match:
        print(i.group())
