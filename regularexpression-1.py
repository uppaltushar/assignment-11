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
match=re.finditer('[+]91-[6-9][0-9]{9}','Mobile Number: +91-8894897895, +91-7986473580 , 3448 ,+91-9459023322')
for i in match:
        print(i.group())
