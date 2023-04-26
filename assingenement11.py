movies = {
   'actors':{
        'prabhas':{'knownAs':'Darling', 'awards':{'nandi':1, 'cinemaa':1, 'siima':1},'remuneration':100,'hits':{'industry':2, 'super':3,'flops':8}, 'age':41, 'height':6.1, 'mStatus':'single','sRate':'35%'},
        'mahesh':{'knownAs':'Prince','awards':{'nandi':8, 'cinemaa':3, 'siima':3},'remuneration':50,'hits':{'industry':2, 'super':6,'flops':11},'age':46, 'height':6.2, 'mStatus':'married','sRate':'46%'},
        'ramcharan':{'knownAs':'Mega Power Star', 'awards':{'nandi':2, 'cinemaa':1, 'siima':1}, 'remuneration':70, 'hits':{'industry':3, 'super':1,'flops':5}, 'age':36, 'height':5.9, 'mStatus':'married', 'sRate':'50%'},
        'ntr':{'knownAs':'Jr NTR', 'awards':{'nandi':2, 'cinemaa':5, 'siima':3}, 'remuneration':70,'hits':{'industry':1, 'super':7,'flops':11}, 'age':36, 'height':5.9, 'mStatus':'married','sRate':'40%'},
        'pavan':{'knownAs':'Power Star', 'awards':{'nandi':2, 'cinemaa':2, 'siima':5}, 'hits':{'industry':2, 'super':7,'flops':16}, 'age':48, 'height':5.9, 'mStatus':'married','sRate':'37%','remuneration':50},
   },
    'actress':{
        'tamanna':{'knownAs':'Milky Beauty', 'awards':{'nandi':0, 'cinemaa':1, 'siima':1}, 'remuneration':10, 'hits':{'industry':1, 'super':7,'flops':11}, 'age':28, 'height':5.9, 'mStatus':'single', 'sRate':'40%'},
        'rashmika':{'knownAs':'Butter Milky Beauty', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2}, 'remuneration':12,'hits':{'industry':0, 'super':4,'flops':2}, 'age':36, 'height':5.9, 'mStatus':'single', 'sRate':'30%'},
        'saipallavi':{'knownAs':'Laughing Queen', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2}, 'remuneration':8,'hits':{'industry':0, 'super':3,'flops':0}, 'age':28, 'height':5.9, 'mStatus':'single', 'sRate':'60%'},
        'samantha':{'knownAs':'Sam', 'awards':{'nandi':2, 'cinemaa':3, 'siima':5},'remuneration':15, 'hits':{'industry':3, 'super':7,'flops':4}, 'age':33, 'height':5.9,'mStatus':'married','sRate':'70%'},
        'kajal':{'knownAs':'Kaj', 'awards':{'nandi':0, 'cinemaa':2, 'siima':2},'remuneration':12,  'hits':{'industry':1, 'super':6,'flops':8}, 'age':35, 'height':5.9, 'mStatus':'married','sRate':'60%'},
    }
}

#1.write a program to disply all actors names?
'''for i in movies['actors']:
    print(i)'''
'''print({i for i in movies['actors']})'''
#2.write a program to disply all actress names?
'''for i in movies['actress']:
    print(i)'''
'''print({i for i in movies['actress']})'''
#3.who is darling?
'''for i in movies['actors']:
    if movies['actors'][i]['knownAs']=='Darling':
        print(i)'''
'''print({i for i in movies['actors'] if movies['actors'][i]['knownAs']=='Darling'})'''
#4.what are the total number of Nandi Awards Won by actors?

'''s=0
for i in movies['actors']:
    s=s+movies['actors'][i]['awards']['nandi']
print(s)'''
'''print({s for i in movies['actors']+movies['actors'][i]['awards']['nandi']})'''
#5.what is the name of prince?
'''for i in movies['actors']:
    if movies['actors'][i]['knownAs']=='Prince':
        print(i)'''
#6.what are the total number of awards own by Ram Charan?

'''s=0
for i in movies['actors']:
    if  'ramcharan' in i:
        s=s+movies['actors'][i]['awards']['nandi']
        s=s+movies['actors'][i]['awards']['cinemaa']
        s=s+movies['actors'][i]['awards']['siima']
        print(s)'''
        
'''s=0
for i in movies['actors']:
    if 'ramcharan' in i:
        s=movies['actors'][i]['awards']
        print(s['nandi']+s['cinemaa']+s['siima'])'''
        
#7.which actor won more number of nandi awards?
'''lst=[]
for i in movies['actors']:
    s=movies['actors'][i]['awards']['nandi']
    lst.append(s)
for i in movies['actors']:
    if movies['actors'][i]['awards']['nandi']==max(lst):
        print(i)'''
'''print({[ movies['actors'][i]['awards']['nandi'] lst.append(s) for i in movies['actors']if movies['actors'][i]['awards']['nandi']==max(list)]})'''
#8.what is the success rate of prince?
'''for i in movies['actors']:
    if movies['actors'][i]['knownAs']=='Prince':
        print(movies['actors'][i]['sRate'])'''
'''print({i for i in movies['actors'] if movies['actors'][i]['konwnAs']=='Prince'movies[['actors'][i]['sRate']})'''
#9.which artist has more number of hits?

'''lst=[]
for i in movies:
    for j in movies[i]:
        s=movies[i][j]['hits']
        lst.append(s['industry']+s['super']+s['flops'])
for i in movies:
    for j in movies[i]:
        s=movies[i][j]['hits']
        if s['industry']+s['super']+s['flops']==max(lst):
            print(j)'''

        
#10.who is milky beauty?
'''for i in movies['actress']:
    if movies['actress'][i]['knownAs']=='Milky Beauty':
        print(i)'''
#11.what is the nic name of resmika?
'''for i in movies['actress']:
    if 'rashmika'in i:
        print(movies['actress'][i]['knownAs'])'''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    
#12.what are actress names who did not win at least one nandi award?
'''lst=[]
for i in movies['actress']:
    s=movies['actress'][i]['awards']['nandi']
    lst.append(s)
for i in movies['actress']:
    if movies['actress'][i]['awards']['nandi']==min(lst):
        print(i)'''
#13.what are the total number of siima awards  own by all artists?
'''s=0
lst=[]
for i in movies:
    for j in movies[i]:
        s=s+movies[i][j]['awards']['siima']
        lst.append(s)
print(s)'''
#14.what is the artist name  who has more success rate?
'''lst=[]
for i in movies:
    for j in movies[i]:
        s=movies[i][j]['sRate']
        lst.append(s)
for i in movies:
    for j in movies[i]:
        if movies[i][j]['sRate']==max(lst):
            print(j)'''
    
    

#15.what is the age of actor who has more super hit movies?
'''lst=[]
for i in movies['actors']:
    s=movies['actors'][i]['hits']['super']
    lst.append(s)
for i in movies['actors']:
    if movies['actors'][i]['hits']['super']==max(lst):
        print(movies['actors'][i]['age'])'''
#16.what is the actress name who is married?
'''for i in movies['actress']:
    if movies['actress'][i]['mStatus']=='married':
        print(i)'''
#17.who is the tallest actor?
'''lst=[]
for i in movies['actress']:
    s=movies['actress'][i]['height']
    lst.append(s)
for i in movies['actress']:
    if movies['actress'][i]['height']==max(lst):
        print(i)'''
#18who is youngest artist?
'''lst=[]
for i in movies:
    for j in movies[i]:
        s=movies[i][j]['age']
        lst.append(s)
for i in movies:
    for j in movies[i]:
        if movies[i][j]['age']==min(lst):
            print(j)'''
#19.who are unmarried actress?
'''for  i in movies ['actress']:
    if movies['actress'][i]['mStatus']!='married':
        print(i)'''
#OR
'''for i in movies ['actress']:
    if movies['actress'][i]['mStatus']=='single':
        print(i)'''
#OR
'''print({i for i in movies['actress']if movies['actress'][i]['mStatus']=='single'})'''
#20.who is the smallest actress?
'''lst=[]
for i in movies['actress']:
    s=movies['actress'][i]['age']
    lst.append(s)
for i in movies['actress']:
    if movies['actress'][i]['age']==min(lst):
        print(i)'''
#OR
'''lst=[]
for i in movies['actress']:
    s=movies['actress'][i]['height']
    lst.append(s)
for i in movies['actress']:
    if movies['actress'][i]['height']==min(lst):
        print(i)'''
#21.which actress has more flops?
'''lst=[]
for i in movies['actress']:
    s=movies['actress'][i]['hits']['flops']
    lst.append(s)
for i in movies['actress']:
    if movies['actress'][i]['hits']['flops']==max(lst):
        print(i)'''
#22.what are the age of butter milky beauty?
'''for i in movies['actress']:
    if movies['actress'][i]['knownAs']=='Butter Milky Beauty':
        print(movies['actress'][i]['age'])'''
#23.what are the total number of flops of all actress?
'''s=0
for i in movies['actress']:
    s=s+movies['actress'][i]['hits']['flops']
print(s)'''
#24.what are the age of sam and kaj?
'''for i in movies['actress']:
    if 'samantha' in i:
        print(movies['actress'][i]['age'])
    if i in 'kajal'in i:
        print(movies['actress'][i]['age'])'''
#25.which actress own highest total number of awards?
'''lst=[]
for i in movies['actress']:
    x=movies['actress'][i]['awards']
    lst.append(x['nandi']+x['cinemaa']+x['siima'])
for i in movies['actress']:
    y=movies['actress'][i]['awards']
    if y['nandi']+y['cinemaa']+y['siima']==max(lst):
        print(i)'''
#26.who is the tallest artis?
'''height=[]
for i in movies:
    for j in movies[i]:
        height.append(movies[i][j]['height'])
for i in movies:
    for j in movies[i]:
        if movies[i][j]['height']==max(height):
            print(j)'''
    
    
#27.what are the total number of industry hits of who has more succes rate?

'''s=0
lst=[]
for i in movies:
    for j in movies[i]:
        x=movies[i][j]['sRate']
        lst.append(x)
for i in movies:
    for j in movies[i]:
        if movies[i][j]['sRate']==max(lst):
            s=movies[i][j]['hits']
print(s['industry']+s['super']+s['flops'])'''
    
    
#28.what is the succes rate of yengest actress'''
'''lst=[]
for i in movies['actress']:
    s=movies['actress'][i]['age']
    lst.append(s)
for i in movies['actress']:
    if movies['actress'][i]['age']==min(lst):
        print(movies['actress'][i]['sRate'])'''
    
    
        
#29.who is youngest married actress
'''lst=[]
for i in movies['actress']:
    if movies['actress'][i]['mStatus']=='married':
        s=movies['actress'][i]['age']
        lst.append(s)
for i in movies['actress']:
     if movies['actress'][i]['age']==min(lst):
        print(i)'''   
        
#30.who is the oldest unmarried actor?
'''lst=[]
for i in movies['actors']:
    if movies['actors'][i]['mStatus']=='single':
        s=movies['actors'][i]['age']
        lst.append(s)
for i in movies['actors']:
    if movies['actors'][i]['age']==max(lst):
        print(i)'''
#31.who are the high successful actor and actress?
'''lst=[]
for i in movies['actors']:
    s=movies['actors'][i]['sRate']
    lst.append(s)
for i in movies['actors']:
    if movies['actors'][i]['sRate']==max(lst):
        print(i)
for i in movies ['actress']:
    s=movies['actress'][i]['sRate']
    lst.append(s)
for i in movies['actress']:
    if movies['actress'][i]['sRate']==max(lst):
        print(i)'''
#OR
'''lst=[]
for i in movies:
    for j in movies[i]:
        s=movies[i][j]['sRate']
        lst.append(s)
for i in movies:
    for j in movies[i]:
        if movies[i][j]['sRate']==max(lst):
            print(j)'''


        

#32.totally how many unmarried artists are acting in movies?
'''lst=[]
for i in movies:
    for j in movies[i]:
        if movies[i][j]['mStatus']=='single':
            lst.append(j)
print(len(lst))'''
    
      
        
#33.which actress is having more industry hit movies?
'''lst=[]
for i in movies['actress']:
    s=movies['actress'][i]['hits']['industry']
    lst.append(s)
for i in movies['actress']:
    if movies['actress'][i]['hits']['industry']==max(lst):
        print(i)'''
#34.which actress does not have atlest one industry hit also?
'''lst=[]
for i in movies['actress']:
    s=movies['actress'][i]['hits']['industry']
    lst.append(s)
for i in movies['actress']:
    if movies['actress'][i]['hits']['industry']==min(lst):
        print(i)'''
#35.what are the total number of industry and supet hits of tallest actress?
'''s=0
lst=[]
for i in movies['actress']:
    x=movies['actress'][i]['height']
    lst.append(x)
for i in movies['actress']:
    if movies['actress'][i]['height']==max(lst):
        s=s+movies['actress'][i]['hits']['industry']
        s=s+movies['actress'][i]['hits']['super']
print(s)'''
                   
##36.which actress is having lengthiest nick name?
'''lst=[]
for i in movies['actress']:
    s=movies['actress'][i]['knownAs']
    lst.append(s)
for i in movies['actress']:
    if  movies['actress'][i]['knownAs']==max(lst):
        print(len(s))'''

        
#37.who are the youngest unmarried artist?
'''lst=[]
for i in movies:
    for j in movies[i]:
        if movies[i][j]['mStatus']=='single':
            s=movies[i][j]['age']
            lst.append(s)
for i in movies:
    for j in movies[i]:
        if movies[i][j]['age']==min(lst):
            print(j)'''



#38.what are the total number of industry hits and super hits of the actress who got more siima awards?
'''s=0
lst=[]
for i in movies['actress']:
    x=movies ['actress'][i]['awards']['siima']
    lst.append(x)
for i in movies['actress']:
    if movies['actress'][i]['awards']['siima']==max(lst):
        s=s+movies['actress'][i]['hits']['industry']
        s=s+movies['actress'][i]['hits']['super']
print(s)'''
    
#39.what are the age of darling and milky beauty?
'''for i in movies['actors']:
    if movies['actors'][i]['knownAs']=='Darling':
        print(movies['actors'][i]['age'])
for i in movies['actress']:
    if movies['actress'][i]['knownAs']=='Milky Beauty':
        print(movies['actress'][i]['age'])'''
#40.what are names of actros whose nick name contains star?
'''for i in movies['actors']:
    s= movies['actors'][i]['knownAs']
    if 'Star' in s:
        print(i)'''
    
    
#41.what is the total remuneration of all actors?
'''s=0
for i in movies['actors']:
    s=s+movies['actors'][i]['remuneration']
print(s)'''
#42.what is the remuneration of an actor who has more flops?
'''lst=[]
for i in movies['actors']:
    s=movies['actors'][i]['hits']['flops']
    lst.append(s)
for i in movies['actors']:
    if movies['actors'][i]['hits']['flops']==max(lst):
        print(movies['actors'][i]['remuneration'])'''
#43.what is the higest remuneration of an unmarries actress?
'''lst=[]
for i in movies['actress']:
    if movies['actress'][i]['mStatus']=='single':
        s=movies['actress'][i]['remuneration']
        lst.append(s)
print(max(lst))'''

#44.what are the name of artists who has more remuneration?
'''lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['remuneration'])
for i in movies:
    for j in movies[i]:
        if movies[i][j]['remuneration']==max(lst):
            print(j)'''

#45.what is the remueration of high successful actress?
'''lst=[]
for i in movies['actress']:
    s=movies['actress'][i]['sRate']
    lst.append(s)
for i in movies['actress']:
    if movies['actress'][i]['sRate']==max(lst):
        print(movies['actress'][i]['remuneration'])'''
#46.what is remuneration of actress who has more industry hits?
'''lst=[]
for i in movies['actress']:
    s=movies['actress'][i]['hits']['industry']
    lst.append(s)
for i in movies['actress']:
    if movies['actress'][i]['hits']['industry']==max(lst):
        print(movies['actress'][i]['remuneration'])'''
#47.what are the ages of an actros whose remuneration is more then 90 crores?
'''for i in movies['actors']:
    if movies['actors'][i]['remuneration']>=90:
        print(movies['actors'][i]['age'])'''
        
#48.what are the total number of industry hits of both prince and butter milky beauty?    
'''s=0
lst=[]
for i in movies['actors']:
    if movies['actors'][i]['knownAs']=='Prince':
        s=s+movies['actors'][i]['hits']['industry']
        lst.append(s)
for i in movies['actress']:
    if movies['actress'][i]['knownAs']=='Butter Milky Beauty':
         s=s+movies['actress'][i]['hits']['industry']
         lst.append(s)
         print(s)'''
'''s=0
lst=[]
for i in movies['actress']:
    if movies['actress'][i]['knownAs']=='Butter Milky Beauty':
        s=s+movies['actress'][i]['hits']['industry']
        lst.append(s)
for i in movies['actors']:
    if movies['actors'][i]['knownAs']=='Prince':
         s=s+movies['actors'][i]['hits']['industry']
         lst.append(s)
print(sum(lst))'''

#49.what is the age of laughing queen?
'''for i in movies['actress']:
    if movies['actress'][i]['knownAs']=='Laughing Queen':
        print(movies['actress'][i]['age'])'''
#50.what are the total number of awards won by an actor who has less  successful rate?
'''lst=[]
s=0
for i in movies['actors']:
    x=movies['actors'][i]['sRate']
    lst.append(x)
    if movies['actors'][i]['sRate']==min(lst):
        s=s+movies['actors'][i]['awards']['nandi']
        s=s+movies['actors'][i]['awards']['cinemaa']
        s=s+movies['actors'][i]['awards']['siima']
print(s)'''
    










    





    
    
