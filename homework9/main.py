#Напишите программу для создания списка, длина которого равна N. После создания 
#списка нужно подсчитать нечетные и четные числа. Если нечетных чисел больше, чем четных, 
#вывод должен быть «Нет», в остальных ключах «Да». 
def even_or_odd(n, arr):
    list_even = []
    list_odd = []
    for num in arr:
        if num % 2 == 0:
            list_even.append(str(num))
        else:
            list_odd.append(str(num))
    print(' '.join(list_odd))
    print(' '.join(list_even))
    print("NO" if len(list_odd) > len(list_even) else "YES")

n = 5
arr = [4, 16, 19, 31, 2]
#n = int(input())
#arr = list(map(int, input().split()))
even_or_odd(n, arr)



#Создайте  вложенный  список  размером  3*3  через  функцию.  И  посчитайте  сумму 
#элементов главной диагонали. 
def main_diagonal():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #matrix = []
    sum = 0
    #for _ in range(3):
        #line = list(map(int, input().split()))
        #matrix.append(line)
    for i in range(3):
        sum += matrix[i][i]
    return f"Diagonals: {matrix[0][0]} + {matrix[1][1]} + {matrix[2][2]} = {sum}"

print(main_diagonal())



#Напишите  программу  СV  (резюме),  которая  будет  считывать  данные  пользователя, 
#через  функцию,  и  выведет  полученные  данные,  при  вызове  в  основном  теле  программы. 
#Шаблон резюме ниже: 
# def create_resume():
#     resume_data = {}
#     resume_data['first_name'] = input("Введите ваше имя: ")
#     resume_data['last_name'] = input("Введите вашу фамилию: ")
#     resume_data['address'] = input("Введите ваш адрес: ")
#     resume_data['phone'] = input("Введите ваш номер телефона: ")
#     resume_data['email'] = input("Введите ваш адрес электронной почты: ")
#     resume_data['linkedin'] = input("Введите URL вашего профиля LinkedIn: ")
#     resume_data['twitter'] = input("Введите URL вашего Twitter/блога/портфолио: ")
#     resume_data['objective'] = input("Введите вашу цель карьеры: ")
#     resume_data['degree1'] = input("Введите ваше первое образование/квалификацию: ")
#     resume_data['school1'] = input("Введите название первого колледжа или университета: ")
#     resume_data['degree2'] = input("Введите ваше второе образование/квалификацию: ")
#     resume_data['school2'] = input("Введите название второго колледжа или университета: ")
#     resume_data['job_title1'] = input("Введите вашу первую должность: ")
#     resume_data['company1'] = input("Введите название первой компании: ")
#     resume_data['job_title2'] = input("Введите вашу вторую должность: ")
#     resume_data['company2'] = input("Введите название второй компании: ")
#     return resume_data

# def print_resume(resume_data):
#     print("\n--- Резюме ---")
#     print(f"Имя: {resume_data['first_name']} {resume_data['last_name']}")
#     print(f"Адрес: {resume_data['address']}")
#     print(f"Телефон: {resume_data['phone']}")
#     print(f"Электронная почта: {resume_data['email']}")
#     print(f"LinkedIn: {resume_data['linkedin']}")
#     print(f"Twitter/Блог/Портфолио: {resume_data['twitter']}")
#     print(f"Цель карьеры: {resume_data['objective']}")
#     print("\n--- Образование ---")
#     print(f"1. {resume_data['degree1']} - {resume_data['school1']}")
#     print(f"2. {resume_data['degree2']} - {resume_data['school2']}")
#     print("\n--- Опыт работы ---")
#     print(f"1. {resume_data['job_title1']} - {resume_data['company1']}")
#     print(f"2. {resume_data['job_title2']} - {resume_data['company2']}")

# #Странная задача
# resume_data = create_resume()
# print_resume(resume_data)



#Написать рекурсивную функцию, которая по заданному целому числу возвращает n-e 
#число Фибоначчи.
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 10
#n = int(input())
print(f"fibonacci number {n} = {fibonacci(n)}")



#Напишите  функцию,  которая  проверяет  является  ли  число  степенью  двойки.  Если 
#истинно выведите True, иначе False. 
def ispower_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

print(ispower_of_two(8))



#Функция в Python — это блок кода, который выполняет определенную задачу и может быть повторно использован.
#Параметры функции — это переменные, которые используются для передачи данных в функцию. 
#Локальные переменные — это переменные, которые объявлены внутри функции и доступны только в пределах этой функции.
#Глобальные переменные — это переменные, которые объявлены вне всех функций и доступны в любой части программы.
#Рекурсивная функция — это функция, которая вызывает саму себя в процессе выполнения. Рекурсия полезна для решения задач, которые могут быть разбиты на более простые подзадачи того же типа. Пример приведен ниже в задании с факториалом числа.



#Напишите функцию print_check, которая 
#принимает список кортежей с информацией о товарах (название, количество, цена) и 
#выводит чек в следующем формате:
def print_check(goods):
    sum = 0
    print('ООО Медовый Гексагон')
    for name, num, price in goods:
        sum += price * num
        print(f'{name} ({num} шт.) - {price} тг.')
    print(f'Итого: {sum} тг.')
    print('Спасибо за покупку!')    

print_check([('honey flower', 7, 1000), ('honey tree', 3, 1250), ('honey raspberry', 10, 2000)])



#Напишите функцию print_person, которая принимает 
#имя и возраст человека и выводит их на экран в формате:
#Добавьте проверку, чтобы функция не принимала возраст меньше 0 или больше 120. В 
#случае недопустимого возраста функция должна выводить сообщение "Invalid age" и 
#завершать работу.
def print_person(name, age):
    if not(0 < age <= 120):
        print("Invalid age")
        return None
    print(f'Name: {name}\nAge: {age}')

print_person('Tom', 37)



#Напишите функцию greet, которая 
#принимает два параметра name и greeting, причём параметр greeting должен быть 
#необязательным и иметь значение по умолчанию "Hello". Функция должна выводить 
#приветствие в формате:
def greet(name, greet = 'Hello'):
    print(f'{greet}, {name}!')

greet('Tom')
greet('Tom', 'Hi')



#Напишите функцию sum_all, которая принимает 
#переменное количество аргументов и возвращает их сумму.
def sum_all(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(sum_all(1, 2, 3))
print(sum_all(5, 10, 15, 20))



#Напишите рекурсивную функцию factorial, которая 
#вычисляет факториал числа.
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

print(factorial(5))