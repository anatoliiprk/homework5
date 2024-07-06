immutable_var = 'Urban', 2, 3.4, [5, 6], True
print('Immutable tuple:', immutable_var)
# immutable_var[1] = 8 Кортеж является неизменяемым объектом
# TypeError: 'tuple' object does not support item assignment
# Но можно изменить значения элементов списка внутри кортежа
immutable_var[3][0] = 7
print('     *Exception:', immutable_var)
mutable_list = ['Urban', 2, 3.4, [5,6], True]
print('Mutable list:', mutable_list)
mutable_list.append('Modified')
print('Mutable list:', mutable_list)
