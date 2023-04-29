employees={
    'emp1':{'name':'Sai','salary':20000,'company':['TCS','capgemini','infosys'],'hTown':'Hyd'},
    'emp2':{'name':'Nani','salary':30000,'company':['Wipro','NTH'],'hTown':'Bangalore'},
    'emp3':{'name':'Satya','salary':40000,'company':['NTH','infosys','CTS'],'hTown':'Chennai'},
    'emp4':{'name':'Rohit','salary':25000,'company':['infosys','TCS','Defteam'],'hTown':'Pune'},
    'emp5':{'name':'Mohan','salary':22000,'company':['NTH','HCL','Deep compute'],'hTown':'Hyd'},
    'emp6':{'name':'Sanjay','salary':45000,'company':['TCS','infosys','Defteam'],'hTown':'Mumbai'}
}
#1.WRITE APROGRAME TO DISPLY  THE SALARY OF SAI?
'''for i in employees:
    if employees[i]['name']=='Sai':
        print(employees[i]['salary'])'''
#2.WRITE A PROGRAME TO DISPLY THE HOME TOWN OF NANI?
'''for i in employees:
    if employees[i]['name']=='Nani':
        print(employees[i]['hTown'])'''
#3.WRITE A PROGRAME TO DISPLY EMPLOYEES NAME WHO IS WORKING IN PUNE?
'''for i in employees:
    if employees[i]['hTown']=='Pune':
        print(employees[i]['name'])'''
#4.WRITE A PROGRAME TO DISPLY ALL COMPANIES NAMES OF SATYA?
'''for i in employees:
    if employees[i]['name']=='Satya':
        print(employees[i]['company'])'''
#5. WRITE A PROGRAME TO DISPLY ALL EMPLOYEES NAMES WHO WORKED IN TCS?
'''for i in employees:
    if'TCS'in employees[i]['company']:
        print(employees[i]['name'])'''
#6.WRITE A PROGRAME TO DISPLY ALL EMPLOYEES NAMES WHO DID NOT WORK IN INFOSYS?
'''for i in employees:
    if 'infosys' not in employees[i]['company']:
        print(employees[i]['name'])'''
#7.WRITE A PROGRAME TO DISPLY ALL EMPLOYEES NAMES?
'''for i in employees:
    print(employees[i]['name'])'''
#8.WRITE A PROGRAME TO DISPLY THE SUM OF SALARIES?
'''x=0
for i in employees:
    x=x+employees[i]['salary']
    print(x)'''
##9. WRITE A PROGRAME TO DISPLY THE LATEST COMPANY OF ROHIT?
'''lst=[]
for i in employees:
    k=employees[i]['name']
    if k=='Rohit':
        k=employees[i]['company']
        print(1[-1])'''
#10.WRITE A PROGRAME TO DISPLY TOTAL COMPANIES COUNT OF SATYA?
'''for i in employees:
    if employees[i]['name']=='Satya':
        print(len(employees[i]['company']))'''
#11.WRITE A PROGRAME TO DISPLY THE EMPLOYEES NAMEWHO IS WORKING IN HCL?
'''for i in employees:
    if 'HCL' in employees[i]['company']:
        print(employees[i]['name'])'''
#12. WRITE A PROGRAME TO DISPLY EMPLOYEES OF NAMES WHO ARE WORKING IN HYD?
'''for i in employees:
    if employees[i]['hTown']=='Hyd':
        print(employees[i]['name'])'''
#13.WRITE A PROGRAME TO DISPLY ALL EMPLOYEES WHOSE NAMES STRATS WITH 'S' CHARECTER?
'''for i in employees:
    if employees[i]['name'].startswith('S'):
        print(employees[i]['name'])'''
#14.WRITE A PROGRAME TO DISPLY ALL EMPLOYEES WHOSE NAME ENDS WITH VOWEL?
'''v='a','e','i','o','i','u'
for i in employees:
    if employees[i]['name'].endswith(v):
        print(employees[i]['name'])'''
#15.WRITE A PROGRAME TO DISPLY THE EMPLOYEES OF NAME WHO WORKED ONLY IN TWO COMPANIES?
'''for i in employees:
    if len(employees[i]['company'])==2:
        print(employees[i]['name'])'''

#16.WRITE A PROGRAME TO DISPLY EMPLOYEES NAMES WHO WORKED IN DEEP COMPUTE?
'''for i in employees:
    if 'Deep compute' in employees[i]['company']:
        print(employees[i]['name'])'''
#17.WRITE A PROGRAME TO DISPLY THE SALARY OF PUNE EMPLOYEE?
'''for i in employees:
    if employees[i]['hTown']=='Pune':
        print(employees[i]['salary'])'''
#18.WRITE A PROGRAME TO DISPLY THE LOCATION OF EMPLOYEES WHO IS TAKING 20000 SALARY?
'''for i in employees:
    if employees[i]['salary']==20000:
        print(employees[i]['hTown'])
    if employees[i]['salary']==20000:
        print(employees[i]['name'])'''
#19.WRITE A PROGRAME TO DISPLY THE SALARYOF SAI AND NANI?
'''for i in employees:
    if employees[i]['name']=='Sai':
        print(employees[i]['salary'])
    if employees[i]['name']=='Nani':
        print(employees[i]['salary'])'''

#20.WRITE A PROGRAME TO DISPLY THE NAME AND SALARY OF BANGALORE EMPLOYEE?
'''for i in employees:
    if employees[i]['hTown']=='Bangalore':
        print(employees[i]['name'])
        print(employees[i]['salary'])'''

