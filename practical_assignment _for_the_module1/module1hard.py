# Данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students_set = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество учеников в список и сортируем его
students_list = list(students_set)
students_list.sort()

# Составляем словарь средних баллов для каждого ученика
average_scores = {}
for i in range(len(students_list)):
    student = students_list[i]  # Получаем имя ученика из списка по индексу
    grade_list = grades[i]  # Получаем список оценок ученика из списка grades по индексу
    average_scores[student] = sum(grade_list) / len(grade_list)

# Вывод результатов
print(average_scores)



