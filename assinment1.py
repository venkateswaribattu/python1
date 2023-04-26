#1.write a programeto check whether a specific player is available in team or not,if not available then append in the team
'''team=['kohli','dhoni','sachin','surya']
name=input('enter any name:')
if name not in team:
    print('{} not in team'.format(name))
if name in team:
    print('{} in team'. format(name))'''
#2.write a programe to check which language by student. if he is learning python then tell him/her that he/ she is learning updated skill otherwise tell him / her to learn python
'''student=input('enter your language:')
gender=input('enter your gender:')
if student in 'python':
    print('{} is leaning python'.format(gender))
else:
    print('{} have to learn python'.format(gender))'''
#3.write a programe to check whether the given number is divisable by 10 or not?
'''n=eval(input('enter any number:'))
if n%10==0:
    print('{} is divisable by 10'.format(n))
else:
    print('{} is not divisable by 10'.format(n))'''
#4.write a programe to check what type of value is given by user?
'''n=eval(input('enter any number:'))
print(type(n))'''
#5.write a programe to check whether a given string is available or not in the string?
'''st='narayana''tech''house'
n=input('enter any string:')
if 'n' in st:
    print('string is available:')
else:
    print('string is not available:')'''
#6. write a programe for following  requerment:
'''monday,tuesday,wednesday,thursday=you can wear school uniform
friday=you can  wear civil dress
saturday=you can wear white and white
sunday=its your choice'''
'''n=input('enter any day:')
if n=='monday'and'tuesday'and'wendnesday'and'thursaday':
    print('you can wear school uniform')
elif n=='friday':
    print('you can wear civil dress')
elif n=='satarday':
    print('you can wear white and white')
elif n=='sunday':
    print('its your choice')
else:
    print('not available')'''
#7.Q.write a programe for following requirement:
'''name=input('enter you are name:')
age=eval(input('enter you are age:'))
if age >=30:
    print('you are age is more than{} then ask him go to marry'.format(age))
elif age>=25:
    print('you are age is more than{} then ask her go to marry'.format(age))
'''    
#8.Q.write a programe for following requrement:
'''name=input('enter you are name:')
gender=input('enter you are gender:')
age=eval(input('enter you are age:'))
if age>=0 and age>=30:
    print('you are ageis more than{} then ask  him go to marry'.format(age))
elif age>=0 and age>=25:
    print('you are age more then{} thenask her go to marry'.format(age))
else:
    print('invalied age')
'''
#9.Q.write a python programe to find BMI(body  mass index)?
'''
weight=float(input('enter your weight(kg):'))
height=float(input('enter your height(cm):'))
def calculation_body_mass_index():
    bmi=weight/(height**2)
    print(bmi)
if bmi<=18.8:
    print('you are under weight')
elif bmi>=andbmi<=24.9:
    print('you are normal weight')
'''
#10.Q.
'''
n=eval(input('enter any number:'))
if n>=1 and n<=10:
    if n%2==0:
        print('you have entered even number')
    else:
        print('you have enterd odd number')
else:
    print('please enter any number between 1and 10')'''

