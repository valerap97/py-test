
from comic_inventory import ComicShop, ComicBook # Импортируем классы ComicShop и ComicBook
from discount_manager import DiscountManager # Импортируем класс DiscountManager
from exceptions import (ComicNotFoundError, NegativeInventoryError, DuplicateISBNError, InvalidDiscountError, ComicNotInStockError) # Импортируем исключения

def main_menu():
    while True:
        print("\nВыберите операцию:")
        print("1. Добавить новый комикс")
        print("2. Найти комикс")
        print("3. Отобразить весь инвентарь")
        print("4. Отобразить доступные скидки")
        print("0. Выйти из программы")

        choice = input("Введите номер операции: ")
        
        if choice == "1":
            add_comic()
        elif choice == "2":
            search_comics_submenu()
        elif choice == "3":
            display_search_results(shop.comics)
        elif choice == "4":
            discount_manager.display_discounts()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте еще раз.")

def add_comic():
    title = input("Введите название комикса: ")
    author = input("Введите автора комикса: ")
    isbn = input("Введите ISBN комикса: ")
    price_str = input("Введите цену комикса: ")
    inventory_count_str = input("Введите количество экземпляров на складе: ")

    try:
        price = float(price_str)
        inventory_count = int(inventory_count_str)
        if price < 0 or inventory_count < 0:
            raise ValueError("Цена или количество не могут быть отрицательными.")
        new_comic = ComicBook(title, author, isbn, price, inventory_count) # Создаем экземпляр ComicBook
        shop.add_comic(new_comic) # Теперь передаем объект new_comic в метод add_comic
        print(f"Комикс '{title}' был успешно добавлен.")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        
def search_comics_submenu():
    while True:
        print("\nВыберите операцию:")
        print("1. Искать по названию")
        print("2. Искать по автору")
        print("3. Искать по ISBN")
        print("4. Назад")

        choice = input("Введите номер операции: ")

        if choice == "1":
            comic = search_comics_by_title(shop)
            display_comic_details(comic)
        elif choice == "2":
            comic = search_comics_by_author(shop)
            display_comic_details(comic)
        elif choice == "3":
            comic = search_comics_by_isbn(shop)
            display_comic_details(comic)
        elif choice == "4":
            return
        else:
            print("Неверный выбор, попробуйте еще раз.")
            continue
        
        if comic:
            comic_operations_submenu(comic)  # Передаем экземпляр ComicBook



def search_comics_by_title(shop):
    title = input("Введите название комикса для поиска: ")
    for comic in shop.comics:
        if comic.title.lower() == title.lower():
            return comic
    print(f"Комиксы с названием '{title}' не найдены.")
    return None

def search_comics_by_author(shop):
    author = input("Введите имя автора для поиска комиксов: ")
    for comic in shop.comics:
        if comic.author.lower() == author.lower():
            return comic
    print(f"Комиксы автора '{author}' не найдены.")
    return None


def search_comics_by_isbn(shop):
    isbn = input("Введите ISBN комикса для поиска: ")
    comic = next((c for c in shop.comics if c.isbn == isbn), None)
    if comic is None:
        print(f"Комикс с ISBN {isbn} не найден.")
    return comic

def display_comic_details(comic):
    print(f"\nНазвание: {comic.title}")
    print(f"Автор: {comic.author}")
    print(f"ISBN: {comic.isbn}")
    print(f"Цена: {comic.price}")
    print(f"Количество на складе: {comic.inventory_count}\n")
    
def display_search_results(comics):
    if comics:
        print("Результаты поиска:")
        for comic in comics:
            print(f"{comic.title} - {comic.author} - {comic.isbn}")
    else:
        print("Комиксы не найдены.")


def comic_operations_submenu(comic):
    while True:
        print("\nВыберите операцию:")
        print("1. Продать комикс")
        print("2. Удалить комикс")
        print("3. Применить скидку на комикс")
        print("4. Редактировать информацию о комиксе")
        print("0. Назад")

        choice = input("Введите номер операции: ")

        if choice == "1":
            sell_comic(comic)
        elif choice == "2":
            remove_comic(comic)
            break
        elif choice == "3":
            if comic:  # Проверяем, что комикс действительно найден
                apply_discount(comic)
            else:
                print("Комикс не найден.")
                break
        elif choice == "4":
            if comic:  # Проверяем, что комикс действительно найден
                edit_comic_info(comic)
            else:
                print("Комикс не найден.")
                break
        elif choice == "0":
            break
        else:
            print("Неверный выбор, попробуйте еще раз.")


def sell_comic(comic):
    try:
        shop.sell_comic(comic)
        print(f"Комикс '{comic.title}' продан.")
    except ComicNotInStockError as e:
        print(e)

def remove_comic(comic):
    try:
        shop.remove_comic(comic)
        print(f"Комикс с ISBN '{comic.isbn}' удален со склада.")
    except ComicNotFoundError as e:
        print(e)

def apply_discount(comic):
    discount_str = input("Введите процент скидки: ")
    try:
        discount = float(discount_str)
        if not (0 < discount <= 100):
            raise InvalidDiscountError("Процент скидки должен быть в диапазоне от 0 до 100.")
        discount_manager.define_discount(comic.isbn, discount)  # передаем ISBN комикса
        print(f"Скидка в размере {discount}% применена к комиксу '{comic.title}' с ISBN '{comic.isbn}'.")
    except (ValueError, InvalidDiscountError) as e:
        print(e)

def edit_comic_info(comic):
    print(f"Редактирование информации о комиксе {comic.title}")
    new_title = input("Введите новое название комикса: ")
    new_author = input("Введите нового автора комикса: ")
    new_price_str = input("Введите новую цену комикса: ")
    
    try:
        new_price = float(new_price_str)
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        shop.edit_comic_info(comic, title=new_title, author=new_author, price=new_price)
        display_comic_details(comic)
    except ComicNotFoundError as e:
        print(e)
    except ValueError as e:
        print(f"Ошибка ввода: {e}")

        
# Инициализация магазина и других компонентов
shop = ComicShop("Мой комикс-магазин")
discount_manager = DiscountManager(shop)

# Основной цикл меню в конце файла
if __name__ == "__main__":
    main_menu()