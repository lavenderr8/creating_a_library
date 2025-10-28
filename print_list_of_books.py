def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
        return

    print("Список книг в библиотеке:\n" + "\n".join(library))


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

book_list_view(library)
book_list_view(empty_library)
