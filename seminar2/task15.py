# Задача №15 
# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

n = int(input("Введите кол-во арбузов: "))
x = int(input("Введите массу арбуза: "))
min_massa, max_massa = x, x
for i in range(n - 1):
    x = int(input("Введите массу арбуза: "))
    if x > max_massa:
        max_massa = x
    elif x < min_massa:
        min_massa = x
print(min_massa, max_massa)