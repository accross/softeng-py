#dicto2.py a dictionary example
#andyp 13.01.13

empNumber = {'Bob' : 1, 'Guido' : 3, 'James' : 7}
print(empNumber['Guido'])
empNumber['nick']=8
print(empNumber)
if 'bob' in empNumber:
    print (empNumber['bob'])
else:
    print ('bob does not exist')
findNum=input()
print(empNumber[findNum])
