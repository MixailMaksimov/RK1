import csv


def print_menu():
    print("Посмотреть список существующих задач - 1")
    print("Создать новую задачу - 2")
    print("Изменить существующую задачу - 3")
    print("Удалить существующую задачу - 4")
    print("Завершить работу - 0 \n")
    x = int(input("Выберете задачу: "))
    print("\n")
    return x


def print_tasks():
    with open("task_book.csv", 'r', encoding='cp1251') as csvf:
        reader = csv.reader(csvf, delimiter=";")
        for row in reader:
            if row:
                print("{:<5} {:<20} {:<5} {:<10} {:<10} {:<12}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        print("\n")
        csvf.close()


def csv_to_list():
    tasks = []
    with open("task_book.csv", 'r', encoding='cp1251') as csvf:
        reader = csv.reader(csvf, delimiter=";")
        for row in reader:
            tasks.append(row)
    csvf.close()
    return tasks


def safe(tasks):
    with open('task_book.csv', 'w', encoding='cp1251', newline='') as csvf:
        writer = csv.writer(csvf, delimiter=";")
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


tasks = csv_to_list()
while True:
    x = print_menu()
    if x == 1:
        print_tasks()
    elif x == 2:
        creat_task(tasks)
        safe(tasks)
    elif x == 3:
        change_task(tasks)
        safe(tasks)
    elif x == 4:
        delite_task(tasks)
        safe(tasks)
    elif x == 0:
        print("Хорошего дня!")
        break
    else:
        print("Команда введена неверно")