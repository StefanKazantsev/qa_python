import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        assert len(collector.books_genre.keys()) == 2

    def test_add_new_book_name_add_more_fourty_symbols_not_added(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить 2')
        assert 'Что делать, если ваш кот хочет вас убить 2' not in collector.get_books_genre()

    def test_set_book_genre_positive_result(self, collector):
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')
        assert collector.get_book_genre('Десять негритят') == 'Детективы'

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book('Карфаген')
        collector.set_book_genre('Карфаген', 'Отсутствующий жанр')
        assert collector.get_book_genre('Карфаген') == ''

    def test_get_book_genre_positive_result(self, collector):
        collector.add_new_book('Агата Кристи')
        collector.set_book_genre('Агата Кристи', 'Детективы')
        assert collector.get_book_genre('Агата Кристи') == 'Детективы'

    def test_get_book_genre_non_existing(self, collector):
         assert collector.get_book_genre('Книга') == None

    def test_get_books_with_specific_genre_positive_result(self, collector):
        collector.add_new_book('Имя розы')
        collector.set_book_genre('Имя розы', 'Детективы')
        collector.add_new_book('Мгла')
        collector.set_book_genre('Мгла', 'Ужасы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Имя розы']

    def test_get_books_with_specific_genre_invalid_genre(self, collector):
        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Фантастика')
        assert collector.get_books_with_specific_genre('Недопстимый жанр') == []

    def test_get_books_for_children_positive_result(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')
        assert collector.get_books_for_children() == ['Дюна']

    def test_add_book_in_favorites_positive_result(self, collector):
        collector.add_new_book('Ярость')
        collector.add_book_in_favorites('Ярость')
        assert 'Ярость' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_non_existing(self, collector):
        collector.add_new_book('Дом у дороги')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_positive_result(self, collector):
        collector.add_new_book('Колобок')
        collector.add_book_in_favorites('Колобок')
        collector.delete_book_from_favorites('Колобок')
        assert 'Колобок' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_non_existing(self, collector):
        collector.delete_book_from_favorites('Золотая рыбка')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_positive_result(self, collector):
        collector.add_new_book('Молчание ягнят')
        collector.add_book_in_favorites('Молчание ягнят')
        collector.add_new_book('Золушка')
        collector.add_book_in_favorites('Золушка')
        assert collector.get_list_of_favorites_books() == ['Молчание ягнят', 'Золушка']

    def test_get_books_genre_positive_result(self, collector):
        collector.add_new_book('Попугай Кеша')
        collector.set_book_genre('Попугай Кеша', 'Мультфильмы')
        collector.add_new_book('Кошмар на улице Вязов')
        collector.set_book_genre('Кошмар на улице Вязов', 'Ужасы')
        assert len(collector.get_books_genre().keys()) == 2
