immutable_var = 1, 2, 'a', 'b'
print (immutable_var)
#невозможно изменить из-за того что Объект «кортеж» не поддерживает назначение элементов
mutable_list = [1, 2, 'ab', 'ba']
mutable_list[0] = 3
print (mutable_list)
