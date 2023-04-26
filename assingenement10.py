#write aprogram to fetch all employees name?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    x=re.findall('[A-Z]{1}[a-z]{1,3}.[A-Z]{1}[a-z]{1,}',i)
    for i in x:
        print(i.replace(' ',''))'''


'''import re
a=open('empdata.txt').read()
m=re.findall('[A-Z]{1}[a-z]{1,3}.[A-Z]{1}[a-z]{1,}',a)
print(m)'''
#2.write a program to featch all mobile numbers from file?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    x=re.findall('[8-9]{1}[0-9]{9}',i)
    for i in x:
      (or)  print(i.replace(' ',''))'''
'''import re
a=open('empdata.txt').read()
m=re.findall('[8-9]{1}[0-9]{9}',a)
print(m)'''
#3.write aprogram to featch all PAN numbers from the file?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    x=re.findall('[A-z]{5}[0-9]{4}[A-Z]{1}',i)
    for i in x:
        print(i.replace(' ',''))'''
'''import re
a=open('empdata.txt').read()
m=re.findall('[A-z]{5}[0-9]{4}[A-Z]{1}',a)
print(m)'''
'''import re
a=open('empdata.txt').read()
m=re.findall('[A-Z]{1,}[0-9]{1,}[A-Z]{1}',a)
print(m)'''
#4.write a program to fetch all email ids from the file?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    x=re.findall('[a-z]{1,}[0-9]*_?[a-z]{0,}?@[a-z]{5}.[a-z]{1,}',i)
    for i in x:
        print(i.replace(' ',''))'''







        
'''import re
a=open('empdata.txt').read()
m=re.findall('[a-z]{1,}[0-9]*_?[a-z]{0,}?@[a-z]{5}.[a-z]{1,}',a)
print(m)'''
#5.write a program to featch all registion number from the file?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    x=re.findall('[A-Z]{2}\s?[0-9]{2}\s?[A-Za-z]{1,}\s?[0-9]{4}',i)
    for i in x:
        print(i.replace('',''))'''
'''import re
a=open('empdata.txt').read()
m=re.findall('[A-Z]{2}\s?[0-9]{2}\s?[A-za-z]{1,}\s?[0-9]{4}',a)
print(m)'''
#6.write a program to all company names?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    y=re.findall('[A-Z]+[a-z]*'' Company',i)
    for i in y:
        print(i.replace(' Company',''))'''
#7.write a program  to fetch all date of birth?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    y=re.findall('[0-9]{1,}/[0-9]{1,}/[0-9]{4}',i)
    for i in y:
        print(i.replace(' ',''))'''
'''import re
a=open('empdata.txt').read()
m=re.findall('[0-9]{1,2}?/[0-9]{1,2}?/[0-9]{4}',a)
print(m)'''
#8.write a program to featch commpany name mr.sai?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    x=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
    if'Mr.Sai'in x:
        y=re.findall('[A-Z]+[a-z]*'' Company',i)
        for i in y:
            print(i.replace(' Company',''))'''
#9.write a program to featch email id of Mr.Rohan?        
'''import re
a=open('empdata.txt').readlines()
for i in a:
    x=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
    if'Mr.Rohan'in x:
        y=re.findall('[a-z]{1,}[0-9]*_?[a-z]{0,}@[a-z]{5}.[a-z]{1,}',i)
        for i in y:
            print(i.replace(' ',''))'''
#10.write a program to featch employees name who is using 9090909090?        
'''import re
a=open('empdata.txt').readlines()
for i in a:
    x=re.findall('[8-9]{1}[0-9]{9}',i)
    if'9090909090'in x:
        y=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
        for i in y:
            print(i.replace(' ',''))'''
#11.write a program to featch pan number of Mr.satya?
        
'''import re
a=open('empdata.txt').readlines()
for i in a:
    x=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
    if'Mrs.Satya'in x:
        y=re.findall('[A-z]{5}[0-9]{4}[A-Z]{1}',i)
        for i in y:
            print(i.replace(' ',''))'''
#12.write a program to featch contact number of both nani and satya?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    x=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
    if'Mrs.Satya'in x:
        y=re.findall('[8-9]{1}[0-9]{9}',i)
        for i in y:
            print(i.replace(' ',''))
    if'Mr.Nani'in x:
        y=re.findall('[8-9]{1}[0-9]{9}',i)
        for i in y:
            print(i.replace(' ',''))'''
#13.write a program to featch emp names of infosys and tcs company?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    x=re.findall('[A-Za-z]{1,}\s[A-Za-z]{1}[a-z]{1,}',i)
    if'TCS Company'in x:
        y=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
        for i in y:
            print(i.replace(' ',''))
    if'Infosys Company'in x:
        y=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
        for i in y:
            print(i.replace(' ',''))'''
#14.write a program to dob of tcs employee?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    x=re.findall('[A-Za-z]{1,}\s[A-Za-z]{1}[a-z]{1,}',i)
    if'TCS Company'in x:
        y=re.findall('[0-9]{1,}/[0-9]{1,}/[0-9]{1,}',i)
        for i in y:
         print(i.replace(' ',''))'''
#15.write a program to featch birth year of mr.Nani?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    x=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)'''
'''import re
a=open('empdata.txt').readlines()
lst=[]
for i in a:
    x=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
    if'Mr.Nani'in x:
         y=re.findall('[0-9]{1,}/[0-9]{1,}/[0-9]{1,}',i)
         y = int(y[0][-4:])
         lst.append(y)
print(y)'''
         


         
#16.write a program to  featch the emp name whose mobile number starts with 8?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    x=re.findall('[8-9]{1}[0-9]{9}',i)
    if x[0][0] in ('[8]'):
        y=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
        for i in y:
            print(i.replace(' ',''))'''
#17.write a program to featch odisha emp name?
'''import re
a=open('empdata.txt').readlines()
for i in a :
    if'OD' in i:
        y=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
        for i in y:
             print(i.replace(' ',''))'''   
#18.write a program to featch youngest employe name?
'''import re
a=open('empdata.txt').readlines()
lst=[]
for i in a:
    x=re.findall('[0-9]{1,2}/[0-9]{1,}/[0-9]{4}',i)
    lst.append(x)
print(min(lst))
for j in a:
    print(j)
    y = re.findall('[0-9]{1,2}/[0-9]{1,}/[0-9]{4}',i)
    print(y)
    if y == min(lst):
        k = re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',j)
            print(k)'''



      
'''import re
a=open('empdata.txt').readlines()
lst=[]
for i in a:
    x=re.findall('[0-9]{1,2}/[0-9]{1,}/[0-9]{4}',i)
    y = int(x[0][-4:])
    lst.append(y)

for k in a:
    m = re.findall('[0-9]{1,2}/[0-9]{1,}/[0-9]{4}',k)
    if int(m[0][-4:])==max(lst):
        print(re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',k))'''
        
 

#19.write a program to featch all male employees name?
'''import re
a=open('empdata.txt').readlines()
lst=[]
for i in a:
   if 'Mr.' in i:
        x=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
        lst.append(x)
        for i in x:
            print(i.replace(' ',''))'''



'''import re
a=open('empdata.txt').readlines()
lst=[]
for i in a:
    x=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
    if 'Mr.' in i:
        lst.append(x)
        for i in x:
            print(i.replace(' ','')'''   
#20.write a program to featch total count of female employees?
'''import re
a=open('empdata.txt').readlines()
lst=[]
for i in a:
    x=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
    if 'Mrs.'in i:
        lst.append(x)
        print(len(lst))'''

#21.write a program to featch all employees names who born in january?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    if'/1/'in i:
        x=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
        for i in x:
            print(i.replace(' ',''))
    if'/01/'in i:
         x=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
         for i in x:
             print(i.replace(' ',''))'''

'''import re
a=open('empdata.txt').readlines()
for i in a:
    if'/1/'in i:
        print(re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i))
    if'/01/'in i:
        print(re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i))'''
#22.write a program to featch contact number of telangana employee?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    if 'TS'in i:
        x=re.findall('[8-9]{1}[0-9]{9}',i)
        for i in x:
            print(i.replace(' ',''))'''
'''import re
a=open('empdata.txt').readlines()
for i in a:
    if 'TS'in i:
        x=re.findall('[8-9]{1}[0-9]{9}',i)
        print(x)'''

#23.write a program to featch company name and mobile number of wipro emplyee?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    if'Wipro'in i:
        x=re.findall('[8-9]{1}[0-9]{9}',i)
        for i in x:
            print(i.replace(' ',''))
for i in a:
    if'Wipro'in i:
        x=re.findall('[A-za-z]{1,}\s[A-Za-z]{1,}',i)
        for i in x:
            print(i.replace(' Company',''))'''
    
#24.write a program to featch emp name who born in leaf year?
'''import re
a=open('empdata.txt').readlines()
lst=[]
lst1=[]
for i in a:
    m=re.findall('[0-9]{1,2}[/][0-9]{1,2}[/][0-9]{4}',i)
    lst.append(m)
for i in lst:
    if int(i[0][-4:])%4==0:
        for x in a:
            if i[0] in x:
                y=re.findall('[Mr]{2}[s]?[.][A-Za-z]{1,}',x)
                print(y)'''

#25.write a program to featch all details of emp whose name not ends with vowel?
'''import re
a=open('empdata.txt').readlines()
for i in a:
    if i[-1] not in 'aeiou':
        x=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
print(i)'''
'''import re
a=open('empdata.txt').readlines()
for i in a:
    if i[-1] not in 'aeiou':
        x=re.findall('[Mr]{2}[s]?[.][A-Z][a-z]*',i)
for i in x:
    print(i.replace(' ','')),'''
