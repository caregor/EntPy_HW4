"""
    ---Task 2---
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
"""


def to_hashable(obj):
    if not isinstance(obj, (str, int, float, tuple)):
        return str(obj)
    return obj


def create_argument_dict(**kwargs):
    argument_dict = {}
    for key, value in kwargs.items():
        key = to_hashable(key)
        value = to_hashable(value)
        argument_dict[value] = key
    return argument_dict


result = create_argument_dict(a=10, b="hello", c=[1, 2, 3])
print(result)
