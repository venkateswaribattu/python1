#.write a program to fetch trainer names?
'''import re
a=open('empdata1.txt').read()
m=re.findall('[Mr]{2}.[A-Z]{1}[a-z]*',a)
print(m)'''
#2.whats are the languages that Mr.Narayana teach?
'''import re
a=open('empdata1.txt').read()
x=re.findall('[Mr]{2}.[A-Z]{1}[a-z]*',a)
if 'Mr.Narayana' in a:
    x=re.findall('[A-z]{1}[a-z]{1,}\sLanguage',a)
    for i in x:
        print(i.replace(' Language',''))'''
#3.what are the mode that mr.Narayana teach?
'''import re
a=open('empdata1.txt').read()
x=re.findall('[Mr]{2}.[A-Z]{1}[a-z]*',a)
if 'Mr.Narayana' in a:
    x=re.findall('[a-z]{1,}\smode,?',a)
    for i in x:
        print(i.replace(' mode',''))'''
    

#4.what are the fee structures of both Python and java?
'''import re
a=open('empdata1.txt').read()
m=re.findall('[0-9]{4}[A-Z]{1}[a-z]{1}',a)
print(m)''''''(or)'''
'''import re
a=open('empdata1.txt').readlines()
for i in a:
    x=re.findall('[0-9]{4}[A-Z]{1}[a-z]{1}',i)
    for i in x:
        print(i.replace(' ',''))'''
'''import re
a=open('empdata1.txt').readlines()
x=re.findall

if 'Python Language'and'Java Language'in a:
    x=re.findall('[0-9]{4}[A-Z]{1}[a-z]{1}',i)
    for i in x:
        print(i.replace(' ',''))'''
    
#5.what  are the courses that Mr.Roshan teach?
'''import re
a=open('empdata1.txt').read()
x=re.findall('[Mr]{2}.[A-Z]{1}[a-z]*',a)
if 'Mr.Roshan' in a:
    x=re.findall('[A-z]{1,}\sCourse',a)
    for i in x:
        print(i.replace(' Course',''))'''



