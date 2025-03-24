# qa_python

    def test_add_new_book_name_add_more_fourty_symbols_not_added(self, collector):
        # Проверяет, что нельзя добавить книгу, если её название длиннее 40 символов.


    def test_set_book_genre_positive_result(self, collector):
        # Проверяет, что можно установить жанр для существующей книги.


    def test_set_book_genre_invalid_genre(self, collector):
        # Проверяет, что нельзя установить жанр, если он не входит в список допустимых жанров.


    def test_get_book_genre_positive_result(self, collector):
        # Проверяет, что можно получить жанр книги по её названию.


    def test_get_book_genre_non_existing(self, collector):
        # Проверяет, что возвращается None, если запросить жанр несуществующей книги.


    def test_get_books_with_specific_genre_positive_result(self, collector):
        # Проверяет, что можно получить список книг с определённым жанром.


    def test_get_books_with_specific_genre_invalid_genre(self, collector):
        # Проверяет, что возвращается пустой список при запросе книг с недопустимым жанром.


    def test_get_books_for_children_positive_result(self, collector):
        # Проверяет, что можно получить список книг, подходящих для детей (без "Ужасов" и "Детективов").


    def test_add_book_in_favorites_positive_result(self, collector):
        # Проверяет, что можно добавить книгу в список "Избранное".


    def test_add_book_in_favorites_non_existing(self, collector):
        # Проверяет, что ничего не происходит, если добавить в "Избранное" несуществующую книгу.


    def test_delete_book_from_favorites_positive_result(self, collector):
        # Проверяет, что можно удалить книгу из "Избранного".


    def test_delete_book_from_favorites_non_existing(self, collector):
        # Проверяет, что ничего не происходит, если удалить из "Избранного" несуществующую книгу.


    def test_get_list_of_favorites_books_positive_result(self, collector):
        # Проверяет, что можно получить список книг из "Избранного".