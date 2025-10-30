def book_list_view(library):
    if not library:
        print(f"В библиотеке нет книг.\n")
        return

    print("Список книг в библиотеке:\n" + "\n".join(library) + "\n")


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
    availability = book['Наличие']

    if availability is None:
        status = "Книга в библиотеке, но её статус не определён"
    elif availability is False:
        status = "Нет в наличии"
    else:
        status = "Есть в наличии"

    print(f"\nИнформация о книге '{title}':",
          f"Автор: {book['Автор']};",
          f"Год издания: {book['Год издания']};",
          f"Наличие: {status}.",
          sep="\n", end="\n\n")


def custom_menu(library):
    menu_selection = {
        1: ("Просмотреть библиотеку.", book_list_view),
        2: ("Добавить книгу.", add_book),
        3: ("Удалить книгу.", remove_book),
        4: ("Выдать книгу.", issue_book),
        5: ("Вернуть книгу.", return_book),
        6: ("Получить информацию о книге.", find_book),
    }

    while True:
        print("\nМеню:")

        for number, (description, _) in menu_selection.items():
            print(f"{number}. {description}")
        print("0. Выйти.\n")

        select_action = input("Выберите пункт из меню: ")

        if select_action == "0":
            print("\nВыход из программы.")
            break

        if not int(select_action) in menu_selection:
            print("Некорректный ввод. Введиде номер пункта повторно.")
            continue

        _, action = menu_selection[int(select_action)]
        if action == add_book:
            title = input("Введите название книги: ")
            author = input("Введите имя автора: ")
            year = input("Введите год издания: ")
            action(library, title, author, int(year))
        elif action in (remove_book, issue_book, return_book, find_book):
            title = input("Введите название книги: ")
            action(library, title)
        else:
            action(library)


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
        "Автор": "Виктор Гюго",
        "Год издания": 1831,
        "Наличие": True
    },
    "Джейн Эйр": {
        "Автор": "Шарлотта Бронте",
        "Год издания": 1847,
        "Наличие": True
    },
}

if __name__ == "__main__":
    custom_menu(library)
