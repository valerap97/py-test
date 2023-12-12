from exceptions import NegativeInventoryError, DuplicateISBNError, ComicNotFoundError, ComicNotInStockError # Импортируем исключе
class ComicBook:
    def __init__(self, title, author, isbn, price, inventory_count):
        if inventory_count < 0:
            raise NegativeInventoryError("Количество экземпляров комикса не может быть отрицательным.")
        self.title = title
        self.author = author
        self.price = price
        self.isbn = isbn
        self.inventory_count = inventory_count

    def update_inventory(self, new_count):
        if new_count < 0:
            raise NegativeInventoryError("Количество экземпляров комикса не может быть отрицательным.")
        self.inventory_count = new_count
        print(f"Инвентарь комикса '{self.title}' обновлен: {self.inventory_count} копий.")

class ComicShop:
    def __init__(self, name):
        self.name = name
        self.comics = []
        self.isbns = set()

    def add_comic(self, comic):
        if comic.isbn in self.isbns:
            raise DuplicateISBNError(f"Комикс с ISBN {comic.isbn} уже существует в магазине.")
        self.comics.append(comic)
        self.isbns.add(comic.isbn)
        print(f"Комикс '{comic.title}' добавлен в магазин '{self.name}'.")
    
    def get_comics_by_title(self, title):
        found_comics = [comic for comic in self.comics if comic.title.lower() == title.lower()]
        if not found_comics:
            raise ComicNotFoundError(f"Комиксы с названием '{title.lower()}' не найдены.")
        return found_comics

    def get_comics_by_author(self, author):
        found_comics = [comic for comic in self.comics if comic.author.lower() == author.lower()]
        if not found_comics:
            raise ComicNotFoundError(f"Комиксы автора '{author.lower()}' не найдены.")
        return found_comics

    def get_comics_by_isbn(self, isbn):
        found_comics = [comic for comic in self.comics if comic.isbn == isbn]
        if not found_comics:
            raise ComicNotFoundError(f"Комикс с ISBN '{isbn}' не найден.")
        return found_comics
    
    def sell_comic(self, comic):
        if comic.inventory_count <= 0:
            raise ComicNotInStockError(f"Нет в наличии комикса '{comic.title}' для продажи.")
        comic.inventory_count -= 1
        print(f"Продана одна копия комикса '{comic.title}'.")

    def display_inventory(self):
        print(f"Инвентарь магазина '{self.name}':")
        for comic in self.comics:
            print(f"Комикс '{comic.title}': {comic.inventory_count} копий.")

    def remove_comic(self, comic):
        if comic not in self.comics:
            raise ComicNotFoundError(f"Комикс '{comic.title}' не найден в магазине.")
        self.comics.remove(comic)
        self.isbns.remove(comic.isbn)
        print(f"Комикс '{comic.title}' удален из магазина.")
    
    def edit_comic_info(self, comic, title=None, author=None, price=None):
        if comic not in self.comics:
            raise ComicNotFoundError(f"Комикс с ISBN '{comic.isbn}' не найден.")

        if title is not None:
            comic.title = title

        if author is not None:
            comic.author = author

        if price is not None:
            comic.price = price

        print(f"Информация о комиксе с ISBN '{comic.isbn}' была обновлена.")
