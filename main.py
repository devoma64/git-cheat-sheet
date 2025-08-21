def print_hello(name):
    return f"Hello, {name}"

print(print_hello("Marv"))

def add(a:int, b:int) -> int:
    return a + b

result = add(5, 5)
# print(result)


def add(a:int , b:int) -> int:
    return a + b
# print(add(5, 5))


# lambda argument: express

add = lambda a, b: a + b
print(add(5,5))
