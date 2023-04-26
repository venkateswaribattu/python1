players={
    'player1':{'name':'Sachin','matches':{'test':200,'odi':463},'scores':{'test':248,'odi':200},'wickets':{'test':46,'odi':154},'age':49,'shirt':10,'role':'top_order','location':'Bombay'},
    'player2':{'name':'Kohli','matches':{'test':102,'odi':262},'scores':{'test':254,'odi':183},'wickets':{'test':0,'odi':4},'age':33,'shirt':18,'role':'top_order','location':'Delhi'},
    'player3':{'name':'Rohit','matches':{'test':44,'odi':231},'scores':{'test':212,'odi':264},'wickets':{'test':2,'odi':8},'age':35,'shirt':45,'role':'opening','location':' Nagpur'},
    'player4':{'name':'Sehwag','matches':{'test':104,'odi':251},'scores':{'test':319,'odi':219},'wickets':{'test':40,'odi':96},'age':43,'shirt':44,'role':'opening','location':'Delhi'},
    'player5':{'name':'Zaheer khan','matches':{'test':92,'odi':200},'scores':{'test':75,'odi':34},'wickets':{'test':311,'odi':282},'age':43,'shirt':41,'role':'Bowler','location':'Bombay'},
    'player6':{'name':'Dhoni','matches':{'test':90,'odi':350},'scores':{'test':224,'odi':183},'wickets':{'test':0,'odi':1},'age':41,'shirt':7,'role':'Keeper','location':'Ranchi'}
}
'''
#1.write a program to display aii players names?
for i in players:
    print(players[i]['name'])'''
#2.write a program to disply ages of players?
'''for i in players:
    print(players[i]['age'])'''
#3.write a program to disply the youngest player name?
'''lst=[]
for i in players:
    lst.append(players[i]['age'])
for i in players:
    if players[i]['age']==min(lst):
        print(players[i]['name'])'''
#4.write a program to disply player name who played more test matches?
'''lst=[]
for i in players:
    lst.append(players[i]['matches']['test'])
    if players[i]['matches']['test']==max(lst):
        print(players[i]['name'])'''
#5.write a program to disply player name and number of test matches who has taken 0 wickets in test matches?
'''for i in players:
    if players[i]['wickets']['test']==0:
        print(players[i]['name'])
    if players[i]['wickets']['test']==0:
        print(players[i]['matches']['test'])'''
#6.write a programe to disply player name who has taken more wickets in odi?
'''lst=[]
for i in players:
    lst.append(players[i]['wickets']['odi'])
for i in players:
    if players[i]['wickets']['odi']==max(lst):
        print(players[i]['name'])'''
#7.write a program to disply players names that played highest number of odi matches?
'''lst=[]
for i in players:
    lst.append(players[i]['matches']['odi'])
    if players[i]['matches']['odi']==max(lst):
        print(players[i]['name'])'''
#8.write a program to disply the player name that has a highest total score of both test and  odi matches?


'''lst=[]
for i in players:
    s=players[i]['scores']
    lst.append(s['test']+s['odi'])
for i in players:
    x=players[i]['scores']
    if x['test']+x['odi']==max(lst):
        print(players[i]['name'])'''

    

#9.write a program to disply total number of matches of kohli?
'''s=0
for i in players:
    if players[i]['name']=='Kohli':
        s=s+players[i]['matches']['odi']
    if players[i]['name']=='Kohli':
        s=s+players[i]['matches']['test']
print(s)'''
#10.write a program to disply the age of rohih?
'''for i in players:
    if players[i]['name']=='Rohit':
        print(players[i]['age'])'''
#11.write a program to disply the total odi scores of all players?
'''lst=[]
s=0
for i in players:
    s=s+players[i]['scores']['odi']
    lst.append(players[i]['scores']['odi'])
    print(s)'''
#12.write a program to disply total number of wickets of zaheer khan?
'''s=0
for i in players:
    if players[i]['name']=='Zaheer khan':
        s=s+players[i]['wickets']['test']
    if players[i]['name']=='Zaheer khan':
        s=s+players[i]['wickets']['odi']
        print(s)'''
#13.write a program to disply all opening batsman names?
'''for i in players:
    if players[i]['role']=='opening':
        print(players[i]['name'])'''
#14.write a program to disply player name that shirt number is highest number?
'''lst=[]
for i in players:
    lst.append(players[i]['shirt'])
for i in players:
    if players[i]['shirt']==max(lst):
        print(players[i]['name'])'''
#15.write a programe to disply all bombay players?
'''for i in players:
    if players[i]['location']=='Bombay':
        print(players[i]['name'])'''
#16.write a programe to disply the shirt number of sachin?
'''for i in players:
    if players[i]['name']=='Sachin':
        print(players[i]['shirt'])'''
#17.write a program to disply the role of rohit in match?
'''for i in players:
    if players[i]['name']=='Rohit':
        print(players[i]['role'])'''
#18.what is the location of the players whose shirt number is 45?
'''for i in players:
    if players[i]['shirt']==45:
        print(players[i]['location'])'''
#19.write a program to disply all wickets of a player whose role is bowler?

'''for i in players:
    if players[i]['role']=='Bowler':
        print(players[i]['wickets'])'''
#20.write a program to count of total number opening players?
'''for i in players:
    if players[i]['role']=='opening':
        if players[i]['role']=='opening':
            print(len(players[i]))'''
    
    

#21.write a program to disply bombay opening player name?
'''for i in players:
    if players[i]['location']=='Bombay':
        if players[i]['role']=='opening':
            print(players[i]['name'])'''
#22.write a program to disply the roles of delhi players?
'''for i in players:
    if players[i]['location']=='Delhi':
        print(players[i]['role'])'''
#23.write a program to disply the role and location of rohit?
'''for i in players:
    if players[i]['name']=='Rohit':
        print(players[i]['role'])
    if players[i]['name']== 'Rohit':   
        print(players[i]['location'])'''
#24.write a program to disply total score of bombay top_order player?
'''s=0
for i in players:
    if players[i]['location']=='Bombay':
        if players[i]['role']=='top_order':
            s=s+players[i]['scores']['test']
            s=s+players[i]['scores']['odi']
            print(s)'''
#25.write a program to disply all uniqe roles of players?
'''for i in players:
    if players[i]['role']=='top_order':
        print(players[i]['name'])
for i in players:
    if players[i]['role']=='opening':
        print(players[i]['name'])'''
#26.write a program to disply shirt number of delhi top_ order player?
'''for i in players:
    if players[i]['location']=='Delhi':
        if players[i]['role']=='top_order':
            print(players[i]['shirt'])'''
#27.write a program to disply keeper name?
'''for i in players:
    if players[i]['role']=='Keeper':
        print(players[i]['name'])'''
#28.write a program to disply the shirt number of dhoni?
'''for i in players:
    if players[i]['name']=='Dhoni':
        print(players[i]['shirt'])'''
#29.write a program to disply names who played less than 100 test matches?
'''for i in players:
    if players[i]['matches']['test']<100:
        print(players[i]['name'])'''
#30.write a program to disply total wickets of ranchi player?
'''s=0
for i in players:
    if players[i]['location']=='Ranchi':
        s=s+players[i]['wickets']['test']
    if players[i]['location']=='Ranchi':
        s=s+players[i]['wickets']['odi']
        print(s)
    '''
