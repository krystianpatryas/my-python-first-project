user_choice = -1

tasks = []

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + "[" + str(task_index) + "]")
        task_index += 1

def add_task():
    task = input('Wpisz treść zadania:')
    tasks.append(task)
    print('Dodano zadanie!')

def delete_task():
    count_in_array = int(input('Podaj numer zadania w tablicy do usunięcia: '))
    tasks.pop(count_in_array)

def save_tasks_to_file():
    file = open('to-do-list.txt', 'w+')
    for task in tasks:
        file.write(task + "\n")
    file.close()

def show_tasks_from_file():
    file = open('to-do-list.txt')
    for line in file.readlines():
        print(line.strip())
    file.close()

while user_choice != 5:

    if user_choice == 0:
        show_tasks_from_file()

    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_task()
        
    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_tasks_to_file()

    print()
    print('0. Wypisz zadania z pliku tekstowego.')
    print('1. Pokaż zadanie')
    print('2. Dodaj zadanie')
    print('3. Usuń zadanie')
    print('4. Zapisz zmiany do pliku')
    print('5. Wyjdź')

    user_choice = int(input('Wybierz liczbę: '))
    print()
