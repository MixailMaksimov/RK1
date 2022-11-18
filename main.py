import csv


def print_menu():
    print("Посмотреть список существующих задач - 1")
    print("Создать новую задачу - 2")
    print("Изменить существующую задачу - 3")
    print("Удалить существующую задачу - 4")
    print("Отсортировать - 5")
    print("Завершить работу - 0 \n")
    x = int(input("Выберете задачу: "))
    print("\n")
    return x


def print_tasks():
    with open("task_book.csv", 'r' ,encoding='cp1251') as csvf:
        reader = csv.reader(csvf, delimiter = ";")
        for row in reader:
            if row:
                print("{:<5} {:<20} {:<5} {:<10} {:<10} {:<12}".format(row[0],row[1],row[2],row[3],row[4],row[5]))
        print("\n")
        csvf.close()


def csv_to_list():
    tasks = []
    with open("task_book.csv", 'r' ,encoding='cp1251') as csvf:
        reader = csv.reader(csvf, delimiter = ";")
        for row in reader:
            tasks.append(row)
    csvf.close()
    return tasks


def safe(tasks):
    with open('task_book.csv', 'w', encoding='cp1251', newline='') as csvf:
        writer = csv.writer(csvf, delimiter = ";")
        for i in range(0, len(tasks)):
            writer.writerow(tasks[i])
    csvf.close()
    print("Файл успешно сохранён.")
    print("\n")


def creat_new_task(count):
    task = []
    task.append(str(count))
    task.append(input("Введите название задачи: \n"))
    task.append(input("Введите время(в формате 'часы':'минуты'): \n"))
    task.append(input("Введите дату (в формате 'день'.'месяц'.'год'): \n"))
    task.append(input("Введите приоритет задачи: \n"))
    task.append(input("Введите статус задачи: \n"))
    print("\n")
    return task


def creat_task(tasks):
    count = len(tasks)
    task = creat_new_task(count)
    tasks.append(task)
    print("Задача добавлена.")
    print("\n")


def delite_task(tasks):
    x = int(input("Введите номер задачи, которую хотете удалить - "))
    tasks.pop(x)
    for i in range(1, len(tasks)):
        tasks[i][0] = str(i)
    print("Задача удалена.")
    print("\n")


def change_task(tasks):
    x = int(input("Введите номер задачи, которую хотете заменить - "))
    task = creat_new_task(x)
    tasks[x] = task
    print("Задача изменена.")
    print("\n")


def sorting_selection():
    print("Выберете кретерий сортировки:")
    print("Номер - 0")
    print("Время - 2")
    print("Дата - 3")
    print("Приоритет - 4")
    print("Статус - 5")
    x = int(input("Введите номер - "))
    print("\n")
    return x


def priority(prior):
    if prior == "Важно":
        x = 1
    else:
        x = 2
    return x


def status(stat):
    if stat == "Выполнено":
        x = 1
    elif stat == "В процессе":
        x = 2
    elif stat == "Не выполнено":
        x = 3
    return x


def sorting(tasks, x):
    if (x == 0) or (x == 2) or (x == 3) :
        for j in range(1, len(tasks)):
            for i in range(2,len(tasks)):
                if tasks[i-1][x] > tasks[i][x]:
                    y = tasks[i-1]
                    tasks[i-1] = tasks[i]
                    tasks[i] = y
    elif x == 4:
        for j in range(1, len(tasks)):
            for i in range(2,len(tasks)):
                if priority(tasks[i-1][x]) > priority(tasks[i][x]):
                    y = tasks[i - 1]
                    tasks[i - 1] = tasks[i]
                    tasks[i] = y
    elif x == 5:
        for j in range(1, len(tasks)):
            for i in range(2,len(tasks)):
                if status(tasks[i-1][x]) > status(tasks[i][x]):
                    y = tasks[i - 1]
                    tasks[i - 1] = tasks[i]
                    tasks[i] = y

tasks = csv_to_list()
while True:
    x = print_menu()
    if x == 1:
        print_tasks()
    elif x == 2:
        sorting(tasks, 0)
        creat_task(tasks)
        safe(tasks)
    elif x == 3:
        sorting(tasks, 0)
        change_task(tasks)
        safe(tasks)
    elif x == 4:
        sorting(tasks, 0)
        delite_task(tasks)
        safe(tasks)
    elif x == 5:
        y = sorting_selection()
        if (y == 0) or (y == 2) or (y == 3) or (y == 4) or (y == 5):
            sorting(tasks, y)
            safe(tasks)
        else:
            print("Сортировка не выполнена! Команда введена неверно.")
            print("\n")
    elif x == 0:
        print("Хорошего дня!")
        break
    else:
        print("Команда введена неверно")