from main import BooksCollector

import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.fixture(scope='session')
    def setup(self):
        return BooksCollector()

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
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre(self, setup):
        setup.add_new_book('Гордость и предубеждение и зомби')
        setup.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert setup.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_book_genre(self, setup):
        assert setup.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre(self, setup):
        setup.add_new_book('Что делать, если ваш кот хочет вас убить')
        setup.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert setup.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби',
                                                                'Что делать, если ваш кот хочет вас убить']

    def test_get_books_for_children(self, setup):
        setup.add_new_book('Маленький принц')
        setup.set_book_genre('Маленький принц', 'Комедии')
        assert setup.get_books_for_children() == ['Маленький принц']

    def test_add_book_in_favorites(self, setup):
        setup.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' in setup.favorites

    def test_get_list_of_favorites_books(self, setup):
        assert setup.get_list_of_favorites_books() == ['Что делать, если ваш кот хочет вас убить']

    def test_delete_book_from_favorites(self, setup):
        setup.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' not in setup.favorites

    def test_get_books_genre(self, setup):
        assert setup.get_books_genre() == {'Гордость и предубеждение и зомби': 'Ужасы',
                                           'Маленький принц': 'Комедии',
                                           'Что делать, если ваш кот хочет вас убить': 'Ужасы'}
