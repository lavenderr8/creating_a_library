def book_list_view(library):
    if not library:
        print(f"В библиотеке нет книг.\n")
        return

    print("Список книг в библиотеке:\n" + "\n".join(library))


def add_book(library, title, author, year):
    if title in library:
        print(f"Книга '{title}' уже существует в библиотеке.")
        update_or_not = input("Хотите обновить информацию о книге? (да/нет): ").lower()
        if update_or_not == "да":
            library[title] = {"Автор": author, "Год издания": year, "Наличие": True}
            print(f"Информация о книге '{title}' успешно обновлена.\n")
        else:
            print("Информация о книге не изменена.\n")
    else:
        library[title] = {"Автор": author, "Год издания": year, "Наличие": True}
        print(f"Книга '{title}' успешно добавлена в библиотеку.\n")


def remove_book(library, title):
    if title not in library:
        print(f"Книга '{title}' не найдена в библиотеке.\n")
        return

    delete_or_not = input(f"Вы точно хотите удалить книгу '{title}'? (да/нет): ").lower()
    if delete_or_not != "да":
        print("Удаление отменено.\n")
        return

    del library[title]
    print(f"Книга '{title}' успешно удалена из библиотеки.\n")


def issue_book(library, title):
    if title not in library:
        print(f"Книга '{title}' не найдена в библиотеке.\n")
        return

    if title in library and library[title]['Наличие'] is False:
        print(f"Невозможно выдать книгу '{title}', так как её нет в наличии.\n")
        return

    library[title]['Наличие'] = False
    print(f"\nКнига '{title}' выдана.\n")


def return_book(library, title):
    if title not in library:
        print(f"Книга '{title}' не принадлежала этой библиотеке.\n")
        return

    if library[title]['Наличие'] is True:
        print(f"Книга '{title}' уже находится в библиотеке.\n")
        return

    library[title]['Наличие'] = True
    print(f"\nКнига '{title}' снова в наличии.\n")


def find_book(library, title):
    if title not in library:
        print(f"Книги '{title}' не найдено в этой библиотеке.\n")
        return
    book = library[title]
    print(f"\nИнформация о книге '{title}':",
          f"Автор: {book['Автор']};",
          f"Год издания: {book['Год издания']};",
          f"Наличие: {'в наличии' if book['Наличие'] else 'нет в наличии'}.",
          sep="\n", end="\n\n")


library = {
    "Грозовой перевал": {
        "Автор": "Эмили Бронте",
        "Год издания": 1847,
        "Наличие": True
    },
    "Скорбь Сатаны": {
        "Автор": "Мария Корелли",
        "Год издания": 1895,
        "Наличие": True
    },
    "Письма Баламута": {
        "Автор": "Клайв Стейплз Льюис",
        "Год издания": 1942,
        "Наличие": False
    },
    "Тихий Дон": {
        "Автор": "Михаил Шолохов",
        "Год издания": 1928,
        "Наличие": False
    },
    "Собор Парижской Богоматери": {
        "Автор": "Викор Гюго",
        "Год издания": 1831,
        "Наличие": True
    },
    "Джейн Эйр": {
        "Автор": "Шарлотта Бронте",
        "Год издания": 1847,
        "Наличие": True
    },
}

empty_library = {}

book_list_view(empty_library)
book_list_view(library)
add_book(library, "Джейн Эйр", "Шарлотта Бронте", 1847)
add_book(library, "Божественная комедия", "Данте Алигьери", 1472)
book_list_view(library)
remove_book(library, "Собор Парижской Богоматери")
book_list_view(library)
issue_book(library, "Джейн Эйр")
issue_book(library, "Оно")
issue_book(library, "Тихий Дон")
return_book(library, "Письма Баламута")
return_book(library, "Убийственное вязание")
return_book(library, "Джейн Эйр")
find_book(library, "Письма Баламута")
find_book(library, "Лаванда и старинные кружева")
