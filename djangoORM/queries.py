import datetime
from datetime import date

from django.db.models import Count, Sum, Q

from models import (
    Author,
    Book,
    Publisher,
    Sales
)


def get_books_count_is_published_after_2000_year():
    """1. Посчитать количесто книг выпущенных после 2000 года"""
    books = Book.objects.filter(
        publish_date__year__gt=2000
    ).count()


def get_author_name_whose_book_not_contain_A_letter():
    """2. Вывести только имена авторов для книг которые не содержат букву А в своем имени"""
    authors = Author.objects.exclude(
        books__name__contains='A'
    ).values_list('name', flat=True)


def get_last_publish_book():
    """3.1. Получить последнюю опубликованную книгу двумя способами"""
    books_1 = Book.objects.order_by('-publish_date').first()
    books_2 = Book.objects.latest('-publish_date')


def get_first_publish_book():
    """3.2. Получить первую опубликованную книгу двумя способами"""
    books_1 = Book.objects.order_by('publish_date').first()
    books_2 = Book.objects.earliest('publish_date')


def get_count_of_books_for_all_authors():
    """4. Посчитать для каждого автора его количество книг"""
    count_of_books = Author.objects.annotate(
        count_of_books=Count('books')
    )


def get_authors_whose_count_of_books_more_than_five():
    """5. Вывести авторов у которых количество книг больше 5, используя метод alias"""
    authors = Author.objects.alias(
        count_of_books=Count('books')
    ).filter(
        count_of_books__gt=5
    )


def return_one_books_name_for_each_year():
    """6. Вывести по одному имени книги для каждого года"""
    names_of_books = Book.objects.distinct('publish_date__year').values_list('name', flat=True)


def get_publish_name_by_qne_query_do_not_load_related_model():
    """7. Одним запросом получить для книг имена паблишеров, не подгружая остальные поля из связанной модели"""
    name_of_publish = Book.objects.select_related(
        'publisher'
    ).only('publisher__name').filter(
        name='some-name'
    )


def execute_some_acting_by_one_query():
    """8. В один запрос для автора выбрать список всех книг исключая id обоих моделей"""
    list_of_books = Book.objects.prefetch_related(
        'authors'
    ).filter(
        authors=1  # author_id
    ).defer('id', 'authors__id')


def write_raw_query():
    """9. С помощью Django ORM написать сырой SQL запрос для получения всех объектов автора"""
    raw_query = Author.objects.raw(
        """select * from books_author;"""
    )


def check_that_book_with_certain_id_is_exist():
    """10. Проверить существует ли книга с id=100"""
    is_book = Book.objects.filter(id=100).exists()


def get_publisher_whose_author_books_birth_day_is_in_sixteen_or_eighteen_century():
    """11. Получить паблишеров у авторов книг которых день рождения в 16 или 18 веке"""
    publishers = Publisher.objects.filter(
        Q(books__authors__birth_day__gte=date(1501, 1, 1), books__authors__birth_day__lte=date(1600, 12, 30)) |
        Q(books__authors__birth_day__gte=date(1701, 1, 1), books__authors__birth_day__lte=date(1800, 12, 30))
    )


def get_or_create_book_with_the_name():
    """12. Создать если не существует книга с именем Эйафьядлаёкюдель"""

    # defaults is parameters that uses only when object don't exist and we are crating its
    # So first check record by following fields: name, price and then if that record don't exist, then will create
    # new record with following fields: name, price, publish_date, publisher_id.
    return Book.objects.get_or_create(
        name='Эйафьядлаёкюдель',
        price=100,
        defaults={
            'publish_date': datetime.datetime.now(),
            'publisher_id': 1
        }
    )


def create_fives_book_by_one_queries():
    """13. Создать 5 книг одном запросом"""
    books = Book.objects.bulk_create(
        [
            Book(name='some_name', publish_date=datetime.datetime.now(), price=100, publisher_id=1),
            Book(name='some_name2', publish_date=datetime.datetime.now(), price=100, publisher_id=1),
            Book(name='some_name3', publish_date=datetime.datetime.now(), price=100, publisher_id=1),
            Book(name='some_name4', publish_date=datetime.datetime.now(), price=100, publisher_id=1),
            Book(name='some_name5', publish_date=datetime.datetime.now(), price=100, publisher_id=1),
        ]
    )


def get_year_of_birth_the_most_ancient_author():
    """14. Получить год рождения самого древнего автора"""
    authors = Author.objects.earliest('birth_day').birth_day


def find_the_most_rich_publication_by_cost_books():
    """15. Найти самое богатое издания по общей стоимости книг"""
    publication = Publisher.objects.annotate(
        total_price=Sum('books__price')
    ).latest('books__price')


def show_list_books_whose_price_is_more_than_sell_price_certain_date():
    """16. Показать список книг цена которых больше цены продаж за 20 февраля 2002 года"""

    """
    To subquery work you need use slice, don't forget about it. For more information to check official documentation.
    books = Book.objects.filter(
        price_test__gte=Subquery(
            Sales.objects.get(
                date__lte=date(2002, 2, 20)
            ).total_sold_usd
        ))
    """
    books = Book.objects.filter(
        price_test__gte=Sales.objects.get(
            date__lte=date(2002, 2, 20)
        ).total_sold_usd
    )
