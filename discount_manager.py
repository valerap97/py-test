from exceptions import ComicNotFoundError, InvalidDiscountError 
class DiscountManager:
    def __init__(self, shop):
        self.shop = shop
        self.discounts = {}

    def apply_discount_to_isbn(self, isbn, discount):
        try:
            comic = self.shop.get_comics_by_isbn(isbn)[0]  # Использование ISBN для идентификации комикса
            comic.price = round(comic.price * (1 - discount / 100), 2)
            print(f"Цена комикса '{comic.title}' со скидкой {discount}% теперь составляет {comic.price}.")
        except ComicNotFoundError as e:
            print(e)
    
    def define_discount(self, isbn, percent):
        if not (0 <= percent <= 100):
            raise InvalidDiscountError("Ошибка: скидка задана некорректно.")
        try:
            self.apply_discount_to_isbn(isbn, percent)
            self.discounts[isbn] = percent
        except ComicNotFoundError as e:
            print(e)

    def display_discounts(self):
            if not self.discounts:  # Проверка пуст ли словарь скидок
                print("Скидок нет!")
            else:
                print("Доступные скидки:")
                for isbn, discount in self.discounts.items():
                    comic = next((comic for comic in self.shop.comics if comic.isbn == isbn), None)
                    if comic:
                        print(f"Комикс '{comic.title}': {discount}% скидка.")
