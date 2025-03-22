from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre.keys()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.fixture
    def collector(self):
        return BooksCollector()

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
