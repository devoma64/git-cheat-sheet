# import function from marv.py
from marv import get_marv_info


def print_hello(name):
    return f"Hello, {name}"

print(print_hello("Marv"))

def add(a:int, b:int) -> int:
    return a + b

result = add(5, 5)
print(result)


print(get_marv_info())