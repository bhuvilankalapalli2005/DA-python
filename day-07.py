#assignmnet operators
x=100
x+=2
print(x)
x-=3
print(x)
x*=2
print(x)
x/=4
print(x)
x//=5
print(x)
x**=2
print(x)
x%=2
print(x)

#membership operators
l=[1,4,5,7,9,0,4,7]
print(100 in l)
name='bhuvansai'
print('z' in name)

#identity operators 
x=[1,2,3]
y=[1,2,3]
print(x is y)
print(x is not y)
a=3
b=3
print(a is b)
print(a is not b)
print(a==b)

#a in python
n='python'
print('a'in 'python')

#5 in [1,3,5,7,9]
a=[1,3,5,7,9]
print(5 in l)

#'java'is not in ['python','c','c++']
b=['python','c','c++']
print('java'not in b)

#10 in (5,10,15,20)
c=(5,10,15,20)
print(10 in c)

#red in list
d=["blue","green","yellow"]
print("red"in d)

#two variables with same value and checking
e=10
f=[10,2,4,6]
print(e is f)

#two list with different list values and checking
g=[1,2,3,4]
h=[5,6,7,8]
print(g is h)

#num checking
num=10
print(num>10 and num<50)

#age
age=17
print(age<18 or age>60)
