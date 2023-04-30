#.write a programe to fetch all even numbers from list?
'''lst=[10,11,13,14,9,8]
lst1=[]
for i in lst:
    if i%2==0:
        lst1.append(i)
print(lst1)'''
#2.write aprograme all string value from string?
'''lst=[10,'a',True,'b',False]
lst1=[]
for i in lst:
    if type(i)is str:
        lst1.append(i)
print(lst1)'''
#3.write a program to fetch all divisable from list?
'''lst=[12,15,27,20,5]
lst1=[]
for i in lst:
    if i%5==0:
        lst1.append(i)
print(lst1)'''
#4.write a programe to count total number of int values in the list?
'''lst=[10,'a',20,True,30,'b',40]
lst1=[]
for i in lst:
    if type(i)is int:
        lst1.append(i)
print(len(lst1))'''
#5.write a programe to count total number of characters in the string(including space)?
'''lst='python language'
print(len(lst))'''
#6.write aprograme to count total numbers of words in the string''
'''st='python narayana tech house hyd'
lst1=st.split()
print(len(lst1))'''
#7.write a programe to fetch all vowles from the string?
'''st='python language'
lst=[]
for i in st:
    if i in 'aeiou':
        lst.append(i)
print(lst)'''
#.write a programe to count total number of vowles?
'''st='python narayana'
n='a','e','i','o','u'
print(len(n))'''
#9.write a programe to total number of charecters in the string(excluding space)?
'''st='python is a simple language'
lst=[]
for i in st:
    if i!=' ':
        lst.append(i)
print(len(lst))'''
#10.write a programe to count total number of consonantes in the string?
'''st='python language'
lst=[]
for i in st:
    if i not in 'aeiou' and i!=' ':
        lst.append(i)
print(len(lst))'''
#11.write a programe to fetch all words which starts witch starts with vowel from given string?
'''st='python is simple and easy language'
lst=[]
lst1=st.split()
for i in lst1:
    if i[0] in 'aeiou':
        lst.append(i)
print(lst)'''
#12.write a programeto fetch all words which ends witch consonent in the given string?
'''st='python is simple and easy language'
lst=[]
lst1=st.split()
for i in lst1:
    if i[-1] not in 'aeiou':
        lst.append(i)
print(lst)'''
#13.write a programe to fetch all words which 'a' two or more then two times?
'''st='python is simple and easy language'
lst=[]
lst1=st.split()
for i in lst1:
    if i.count('a')>=2:
        lst.append(i)
print(lst)'''
#14.write a programe to charecters of each worad in the string?
'''st='python is simple and easy language'
lst=[]
lst1=st.split()
for i in lst1:
    x=len(i)
    lst.append(x)
print(lst)'''
#15.write a programe to fetch the first and last charater from each word in string?
'''st='python is simple and easy language'
lst=[]
lst1=st.split()
for i in lst1:
    lst.append(i[0]+i[-1])
print(lst)'''
#16.write a programe to fetch all words which contain 'a' charater in string?
'''st='python is simple and easy language'
lst=[]
lst1=st.split()
for i in lst1:
    if 'a' in i:
        lst.append(i)
print(lst)'''
#17.write a programe to fetch all words which does not contian 'e'charater in the string?
'''st='python is simple and easy language'
lst=[]
lst1=st.split()
for i in lst1:
    if 'e'not in i:
        lst.append(i)
print(lst)'''
#18.write a programe to fetch all words which contains onli 4 or lessthen 4 chareters?
'''st='python is simple and easy language'
lst=[]
lst1=st.split()
for i in lst1:
    if len(i)<=4:
        lst.append(i)
print(lst)'''
#19.write a programe to fetch all words which contain odd number of charter in the string?
'''st='python is simple and easy language'
lst=[]
lst1=st.split()
for i in lst1:
    if len(i)%2==1:
        lst.append(i)
print(lst)'''
#20.write a programe to fetch all words starts and ends with vowel in the string?
'''st='python is number one language'
lst=[]
lst1=st.split()
for i in lst1:
    if i[0]in('aeiou') and i[-1]in('aeiou'):
        lst.append(i)
print(lst)'''
#21.write a programe to fetch all pelindrome words from list?
'''lst=['madam','python','dad','language','eye','malayalam']
lst1=[]
for i in lst:
    if i[-1::-1] in i:
      lst1.append(i)
print(lst1)'''
#22.write a programe to fetch all non-pelindrame words from list?
'''lst=['madam','python','dad','language','eye','malayalam']
lst1=[]
for i in lst:
    if i[-1::-1] not in i:
        lst1.append(i)
print(lst1)'''
#23.write a programe to fetch all palindram words which starsts with 'm'character?
'''lst=['madam','python','dad','language','eye','malayalam']
lst1=[]
for i in lst:
    if i[-1::-1] in lst and i.startswith('m'):
        lst1.append(i)
print(lst1)'''

        
#24.write a proagrame to fetch all palindram words which  more then 3 character?
'''lst=['madam','python','dad','language','eye','malayalam']
lst1=[]
for i in lst:
    if i[-1::-1] in lst and len(i)>3:
        lst1.append(i)
print(i)'''
#25.write a programe to longest palindrome word'''
'''st=['madam','python','dad','language','eye','malayalam']
lst=[]
lst1=[]
for i in st:
    if i[-1::-1]==i:
        lst.append(i)
        lst.append(len(i))
for i in lst:
    if len(i)==max(lst1):
        print(i)'''
