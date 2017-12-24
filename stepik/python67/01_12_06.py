﻿# [STEPIK]
# Программирование на Python https://stepik.org/67
# 01_12_06 Задачи по материалам недели

'''
В институте биоинформатики по офису передвигается робот. 
Недавно студенты из группы программистов написали для него программу, по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов".

Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное окончание слова.

Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное), выводящее это число в консоль вместе с правильным образом изменённым словом "программист", для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.

В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.

Дополнительный комментарий к условию:
Обратите внимание, что задача не так проста, как кажется на первый взгляд. 
Если ваше решение не проходит какой-то тест, это значит, что вы не рассмотрели какой-то из случаев входных данных (число программистов 0≤n≤1000). 
Обязательно проверяйте свои решения на дополнительных значениях, а не только на тех, что приведены в условии задания. 

Так как задание повышенной сложности, вручную код решений проверяться не будет. 
Если вы столкнулись с ошибкой в первых четырёх тестах, проверьте, что вы используете только русские символы для ответа. В остальных случаях ищите ошибку в логике работы программы.

Sample Input 1:
5
Sample Output 1:
5 программистов

Sample Input 2:
0
Sample Output 2:
0 программистов

Sample Input 3:
1
Sample Output 3:
1 программист

Sample Input 4:
2
Sample Output 4:
2 программиста
'''

n = int(input())

ending = 'ов'

if (n % 100 == 11) or (n % 100 == 12) or (n % 100 == 13) or (n % 100 == 14):
	ending == 'ов'
elif n % 10 == 1:
	ending = ''
elif (n % 10 == 2) or (n % 10 == 3) or (n % 10 == 4):
	ending = 'а'
else:
	ending == 'ов'
	
print(str(n) + ' программист' + ending)