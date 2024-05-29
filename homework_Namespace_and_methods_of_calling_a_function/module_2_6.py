def single_root_words(root_word, *other_words):
    # Приводим root_word к нижнему регистру
    root_word_lower = root_word.lower()

    # Инициализируем пустой список для подходящих слов
    same_words = []

    # Перебираем все слова в other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()

        # Проверяем, содержит ли слово root_word или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            # Если условие выполнено, добавляем слово в same_words
            same_words.append(word)

    # Возвращаем список подходящих слов
    return same_words


# Пример использования функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выводим результаты на консоль
print(result1)
print(result2)
