def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
        return

    print("Список книг в библиотеке:\n" + "\n".join(library))


def add_book(library, title, author, year):
    if title in library:
        print(f"Книга '{title}' уже существует в библиотеке.")
        choice = input("Хотите обновить информацию о книге? (да/нет): ").strip().lower()
        if choice == "да":
            library[title] = {"author": author, "year": year, "availability": None}
            print(f"Информация о книге '{title}' успешно обновлена.\n")
        else:
            print("Информация о книге не изменена.\n")
    else:
        library[title] = {"author": author, "year": year, "availability": None}
        print(f"Книга '{title}' успешно добавлена в библиотеку.\n")


library = {
    "Wuthering Heights": {"author": "Emily Brontë",
                          "year": 1847,
                          "availability": "available"},
    "The Sorrows of Satan": {"author": "Marie Corelli",
                             "year": 1895,
                             "availability": "available"},
    "The Screwtape Letters": {"author": "Clive Staples Lewis",
                              "year": 1942,
                              "availability": "not available"},
    "And Quiet Flows the Don": {"author": "Mikhail Sholokhov",
                                "year": 1928,
                                "availability": "not available"},
    "Notre-Dame de Paris": {"author": "Victor Hugo",
                            "year": 1831,
                            "availability": "available"},
    "Jane Eyre": {"author": "Charlotte Brontë",
                  "year": 1847,
                  "availability": "available"}
}

empty_library = {}

add_book(library, "Jane Eyre", "Charlotte Brontë", 1847)
add_book(library, "The Divine Comedy", "Dante Alighieri", 1472)

book_list_view(library)
book_list_view(empty_library)
