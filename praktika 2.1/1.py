J = input("Введите строку драгоценностей (J): ")
S = input("Введите строку камней (S): ")
def array(J, S):
    jewels = set(J)
    count = 0
    for stone in S:
        if stone in jewels:
            count += 1
    return count
result = array(J, S)
print(f"Количество драгоценностей в камнях: {result}")
