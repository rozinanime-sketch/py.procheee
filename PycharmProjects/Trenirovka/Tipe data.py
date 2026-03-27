import sys

print("+" * 90)
print("Тип данных     | Тип в Python      | Что это?  | Размер в байтах")
print("+" * 90)

print(f"bool           | bool               | класс     | {sys.getsizeof(False)}")
print(f"int            | int                | класс     | {sys.getsizeof(0)}")
print(f"float          | float              | класс     | {sys.getsizeof(0.0)}")
print(f"complex        | complex            | класс     | {sys.getsizeof(0j)}")
print(f"str            | str                | класс     | {sys.getsizeof('')}")
print(f"bytes          | bytes              | класс     | {sys.getsizeof(b'')}")
print(f"bytearray      | bytearray          | класс     | {sys.getsizeof(bytearray())}")
print(f"list           | list               | класс     | {sys.getsizeof([])}")
print(f"tuple          | tuple              | класс     | {sys.getsizeof(())}")
print(f"set            | set                | класс     | {sys.getsizeof(set())}")
print(f"dict           | dict               | класс     | {sys.getsizeof({})}")
print(f"NoneType       | None               | класс     | {sys.getsizeof(None)}")

print("+" * 90)
