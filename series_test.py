import pandas as pd

sel1 = pd.Series([10,20,30,40], index =['홍길동','이순신','김유신','강감찬'])
print(sel1)
print("---------------")
print(sel1[['홍길동','강감찬']])
print("---------------")
print(sel1.index)
print(sel1.values)
print(sorted(sel1.index))
print("---------------")
list1 = [1,2,4,5,6,7,7,1,4,4,]
se2 = pd.Series(list1) #List1을 Series로 변환
se2_unique = pd.unique(se2)
print(se2_unique)
print("---------------")
age = {'홍길동' : 23, '김유신' : 30, '이순신' : 40, '강감찬': 31}
se3 = pd.Series(age)
print(se3)