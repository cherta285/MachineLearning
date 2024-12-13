#y=x1 + 2*x2 + 3*x3

from random import randint
from sklearn.linear_model import LinearRegression

#Создание тренировочного набора данных
train_set_limit = 1000
train_set_count = 100

train_input = list()
train_ouptput = list()
for i in range(train_set_count):
    a = randint(0, train_set_limit)
    b = randint(0, train_set_limit)
    c = randint(0, train_set_limit)
    op = a+(2*b)+(3*c)
    train_input.append([a,b,c])
    train_ouptput.append([op])
    
for i in range(20):
    print(train_input[i],train_ouptput[i]) 

#Тренировка
predicator = LinearRegression()
predicator.fit(X=train_input, y=train_ouptput)

#Прогнозирование
x_test = [[10,20,30]]
outcome = predicator.predict(X=x_test)
coefficients = predicator.coef_

print('Outcome:', outcome)
print('Coefficient:', coefficients)
