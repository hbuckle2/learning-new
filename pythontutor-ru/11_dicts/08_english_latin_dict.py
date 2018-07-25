"""
http://pythontutor.ru/lessons/dicts/problems/english_latin_dict/
Однажды, разбирая старые книги на чердаке, школьник Вася нашёл англо-латинский словарь.
Английский он к тому времени знал в совершенстве, и его мечтой было изучить латынь. Поэтому попавшийся словарь был как раз кстати.

К сожалению, для полноценного изучения языка недостаточно только одного словаря: кроме англо-латинского необходим латинско-английский.
За неимением лучшего он решил сделать второй словарь из первого.

Как известно, словарь состоит из переводимых слов, к каждому из которых приводится несколько слов-переводов.
Для каждого латинского слова, встречающегося где-либо в словаре, Вася предлагает найти все его переводы (то есть все английские слова, для которых наше латинское встречалось в его списке переводов), и считать их и только их переводами этого латинского слова.

Помогите Васе выполнить работу по созданию латинско-английского словаря из англо-латинского.

В первой строке содержится единственное целое число N — количество английских слов в словаре. Далее следует N описаний.
Каждое описание содержится в отдельной строке, в которой записано сначала английское слово, затем отделённый пробелами дефис, затем разделённые запятыми с пробелами переводы этого английского слова на латинский.
Все слова состоят только из маленьких латинских букв. Переводы отсортированы в лексикографическом порядке. Порядок следования английских слов в словаре также лексикографический.

Выведите соответствующий данному латинско-английский словарь, в точности соблюдая формат входных данных.
В частности, первым должен идти перевод лексикографически минимального латинского слова, далее — второго в этом порядке и т.д.
Внутри перевода английские слова должны быть также отсортированы лексикографически.
"""

d = {}
for _ in range(int(input())):
    eng, words = input().split(' - ')
    for word in words.split(','):
        word = word.strip()
        if word not in d:
            d[word] = eng
        else:
            if type(d[word]) != list:
                vals = [d[word]]
            else:
                vals = []
                vals.extend(d[word])
            d[word] = vals
            d[word].append(eng)

print(len(d))
for k in sorted(d):
    print(k, '-', end=' ')
    if type(d[k]) == list:
        print(', '.join(sorted(d[k])))
    else:
        print(d[k])