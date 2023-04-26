#1.write a progam to fetch all data from the file.
'''print(open('nthdata.txt').read())'''
#2.write a program to read the frist line from the file.
'''print(open('nthdata.txt').readline())'''
#3.write a program to read the last line from the file.
'''print(open('nthdata.txt').readlines()[-1])'''
#4.write a program to read the third line from the file.
'''print(open('nthdata.txt').readlines()[2])'''
#5.write a programe to count total number of chareactars in the file.
'''print(len(open('nthdata.txt').read()))'''
#6.write a program to count total number of commas in the file.
'''print(open('nthdata.txt').read().count(','))'''
#7.write a program to count total number of words in the first line.
'''print(len(open('nthdata.txt').readlines()[0].split(',')))'''
#8.write a program to count total number of lines in the file.
'''print(len(open('nthdata.txt').readlines()))'''
#9.write a programe to count total number of sai name in the file.
'''print(open('nthdata.txt').read().split(',').count('Sai'))'''
#10.write a program to fetch the word from the each line  in the file.
'''print([i.split(',')[0] for i in open('nthdata.txt').readlines()])'''
#11.write a program to featch the last word from the each line.
'''print([i.replace('\n','').split(',')[-1] for i in open('nthdata.txt').readlines()])'''
#12.write a program to featch all words witch starts with 'a' chareter.
'''print([i for i in open('nthdata.txt').read().replace('/n',',').split(',') if i[0].lower() in 'a'] )'''
#13.write a program to featch all words which ends with an vowel.
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i[-1].lower() in 'aeiou'])'''
#14.write a program to featch all words which has eaither 'a' or 'i'chreacter in the file.
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if 'a'in i or 'i' in i])'''
#15.write a program to featch all words which coantain only 5 charecters in the file.
'''print([i for i in open('nthdata.txt').read().replace('/n',',').split(',') if len(i)==5])'''
#16.write a program to featch all words which does not containes vowels except i in the file.
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if 'aeou' not in i])'''
#17.write a program to  featch all words which ends with uppercase character in the file.
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i.isupper()])'''
#18.write a programe to count total number of  chareter in the file excluding commas and '\n'.
'''print(len([i for i in open('nthdata.txt').read() if i!= ',' and '\n']))'''
#19.write a program to count total number of words in the entair file?
'''print(len(open('nthdata.txt').read().replace('\n',',').split(',')))'''
#20.write a program to featch all even numbers words from from every entair line in the file.
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if len(i)%2==0])'''
#21.write a program to featch all words which ends with bha in the file.
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i.endswith('bha')])'''
#22.write a program to desply  all tcsemployees.
'''print([i for i in open('nthdata.txt').readline() if i in 'TCS'])'''
#23.wite a program to disply the company name of  chinna employee?
'''print([i.replace('\n',',').split(',')[0] for i in open('nthdata.txt').readlines() if 'Chinna' in i])'''
#24.write a programe to  featch the 2nd from 3rd line in the file?
'''print(open('nthdata.txt').readlines()[2].split(',')[1])'''
#25 write a program to featch the first and last character of each word in the third line.
'''print([i[0]+i[-1] for i in open('nthdata.txt').readlines()[2].split(',')])'''
#26.write a program to  featch first and last charecter of each word in the last line?
'''print([i[0]+i[-1] for i in open('nthdata.txt').readlines()[5].split(',')])'''
#27.write a program to featch all characters (except 1st  and last chars)of each word in the 3rd line?
'''print([i[1:-1] for i in open('nthdata.txt').readlines()[1].split(',')])'''
#28.write a program to count total number of words which starts with's charater?
'''print(len([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i.startswith('S')]))'''
#29.write a program to featch all duplicate names in the file?
'''
print(list([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if open('nthdata.txt').read().replace('\n',',').split(',').count(i)>=2]))
'''
#30.write a program to count all vowels in the file?(out put must be dic)
'''data=open('nthdata.txt')
b=readlines().replace('\n',',').split(',')
v='aeiouAEIOU'
d={}.fromkeys(v,0)
for i in b:
    if i in v:
        d[i]=d[i]+1
print(d)'''
    
#31.write a program to reverse all words in the file?
'''print(open('nthdata.txt').read().replace('\n',',').split(',') [-1::-1])'''
#32.write a program to fetch all words which contains two or more then 'a' characters?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i.count('a')>=2])'''
#33.write a program to fetch all words which starts and ends with 'a 'charater?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i.lower().startswith('a') and i.endswith('a')])'''
#34.write a program to fetch word which has more number of 'a'charater?
'''a=open('nthdata.txt').read().replace('\n',',').split(',')
lst=[]
for i in a:
    lst.append(i.lower().count('a'))
    if i.lower().count('a')==max(lst):
        print(i)'''
    
#35.write a program to fetch all company name which starts with vowel?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i[0] in 'AEIOU'])'''
#36.write a program to disply company name which contain saroja employee?
'''print([i.replace('\n',',').split(',')[0] for i in open('nthdata.txt').readlines() if 'Saroj'in i])'''
#37.write a program to count all words which starts and ends with consonants?
'''print(len([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i[0].lower() not in 'aeiou'and i[-1].lower() not in 'aeiou']))
'''
#38.write a program to featch all company names which does not contain venkat employee?
'''print([i.replace('\n',',').split(',')[0] for i in open('nthdata.txt').readlines()if 'Venkat' not in i])'''
#39.write a program to dispy company name where narayana is working?
'''print([i.replace('\n',',').split(',')[0] for i in open('nthdata.txt').readlines()if 'Narayana' in i])'''
#40.write a program to disply the first  word and last word  from each line in tha dict format?
'''data=open('nthdata.txt').readlines()
fword=[]
lword=[]
for i in data:
    x=i.replace('\n','').split(',')
    fword.append(x[0])
    lword.append(x[-1])
    d={}
    for key,values in zip(fword,lword):
        d[key]=values
print(d)'''
#41.write a program to fetch all names whose name starts with 'a' in nth company?
'''print([i for i in [i.split(',')[1:]for i in open('nthdata.txt').readlines()if i.split(',')[0]=='NTH'[0]if i.startswith('A')]])'''
#42.write a program to count total number of employees in cts company?
'''print([len(i.replace('\n','' ).split(',')[1:]) for i in open('nthdata.txt').readlines() if 'CTS' in i])'''
#43.write a program to fetch all companies where venkat employees is working?
'''print([i.replace('\n',',').split(',')[0] for i in open('nthdata.txt').readlines() if 'Venkat'in i])'''
#44.write a program to fetch all companies names which name starts vowel?
'''print([i.replace('\n',',').split(',')[0] for i in open('nthdata.txt').readlines() if i.lower()[0] in 'aeiou'])'''
#45.write a program to fetch all paliendrame names from the file?
'''print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i.lower()== i[-1::-1].lower()])'''
#46.write a program to fetch all companies names where palindrome named employees working?
a=(open('nthdata.txt').readlines())
for i in a:
    t=i.replace('\n','').split(',')[1:]
    for j in t:
        if j.lower()==j[-1::-1].lower():
            print(i.split(',')[0])
    
        

#47.write a program to fetch all the lengthiest company name?
'''
lst=[]
a=(open('nthdata.txt').readlines())

coms = []
lens = []
for i in a:
    coms.append(i.split(',')[0])
    lens.append(len(i.split(',')[0]))
    
for i in coms:
    if len(i) == max(lens):
    print(i)'''
'''
for i in a:
    t=i.split(',')
    print(i.split(',')[0])
for i in t:
    lst.append(len(i))
for i in t:
    if len(i)== max(lst):
        print(i)
   ''' 
        
#48.write a program to fetch the lengthiest employee name in abc company?
'''data=open('nthdata.txt').readlines()
for i in data:
    if i.split(',')[0]=='ABC':
        x=i.split(',')[1:]
        lst1=[]
for i in x:
    lst1.append(len(i))
for i in x:
    if len(i)==max(lst1):
        print(i)'''
#49.write a program to fetch shortest employee name in the wipro company?
'''data=open('nthdata.txt').readlines()
for i in data:
    if i.split(',')[0]=='WIPRO':
        x=i.split(',')[1:]
        lst1=[]
for i in x:
    lst1.append(len(i))
for i in x:
    if len(i)==min(lst1):
        print(i)'''
#50.write a program count total number of employees in each company (in dict format)?
'''companies=[i.split(',')[0] for i in open('nthdata.txt').readlines()]
d={}.fromkeys(companies,0)
for i in open('nthdata.txt').readlines():
    if i.split(',')[0]in d:
        x=len(i.split(',')[1:])
        d[i.split(',')[0]]=d[i.split(',')[0]]+x
print(d)'''
