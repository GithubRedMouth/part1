s = r'C:\d\new.txt'  # чтобы не ставить двойной апостров нужно в начале r

s = 'Py' 'thon' #для пайтона пробел тут ничего не значит

s1 = 'Hello, '
s2 = 'world!'
s3 = s1 + s2# строки можно объеденить и выведет Hello python

name = 'John'
age = 20

print('My name is ' + name + " I'm " + str(age))# тут вывод с переменными и int нужно перевести в str

print('hi ' * 5)# если умножить число на строку выведет hihihihihi

s = 'Hello world!'
print(s[0])
print(s[-12]) # тут у нас индексация и ссчет начинается с 0

print(s[0:12]) #вывод Hello world! потому что промежуток обозначен вся строка
print(s[-1]) #так как тут отрицательное то отсчет начинается с последнего индекса
print(s[0:5]) #можно не указывать 0 так как по умолчанию там стоит 0
print(s[:5]) #тут не укозали
print(s[6:]) #можно и конец диапазона не указывать
print(s[::2]) #тут шаг т.е. он пропускает каждую второй индекс
print(s[::-1]) #выводит наоборот
print(s[:5] + s[6:]) #пропустили пробел


